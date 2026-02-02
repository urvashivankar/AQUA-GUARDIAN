import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';
import { Menu, User, LogOut, Droplets } from 'lucide-react';
import { useAuth } from '@/contexts/AuthContext';
import { Link } from 'react-router-dom';

const Navbar = () => {
  const { user, logout, isAuthenticated } = useAuth();
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = [
    { href: '/', label: 'Home' },
    { href: '/dashboard', label: 'Dashboard' },
    { href: '/report', label: 'Report Pollution' },
    { href: '/marine-impact', label: 'Marine Impact' },
    { href: '/community-action', label: 'Community Action' },
    { href: '/leaderboard', label: 'Leaderboard' },
    { href: '/how-to-use', label: 'How to Use' },
  ];

  const filteredNavLinks = navLinks.filter(link => {
    if (link.href === '/report') {
      const role = user?.role?.toLowerCase();
      if (role === 'government' || role === 'ngo') return false;
    }
    return true;
  });

  return (
    <nav className="ocean-card border-b sticky top-0 z-50 backdrop-blur-lg animate-fade-in">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center space-x-3 group">
            <div className="relative flex items-center justify-center">
              <div className="absolute inset-0 bg-ocean-primary/20 blur-lg rounded-full group-hover:bg-ocean-primary/30 transition-all duration-500"></div>
              <div className="relative bg-gradient-to-br from-ocean-primary/20 to-ocean-light/10 p-2 rounded-xl border border-ocean-primary/20 group-hover:border-ocean-primary/40 transition-all duration-300 backdrop-blur-sm">
                <svg
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  className="text-ocean-primary group-hover:scale-110 transition-transform duration-500"
                >
                  <path
                    d="M12 22C12 22 20 18 20 12V5L12 2L4 5V12C4 18 12 22 12 22Z"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                  <path
                    d="M12 17C13.6569 17 15 15.6569 15 14C15 12.3431 12 9 12 9C12 9 9 12.3431 9 14C9 15.6569 10.3431 17 12 17Z"
                    fill="currentColor"
                  />
                </svg>
              </div>
            </div>
            <span className="text-xl font-bold text-ocean-light tracking-tight group-hover:text-white transition-colors">
              Aqua <span className="text-ocean-primary">Guardian</span>
            </span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden lg:flex items-center space-x-6">
            {filteredNavLinks.map((link) => (
              <Link
                key={link.href}
                to={link.href}
                className="text-muted-foreground hover:text-ocean-light transition-colors duration-200 text-sm font-medium"
              >
                {link.label}
              </Link>
            ))}
          </div>

          {/* User Actions */}
          <div className="flex items-center space-x-4">
            {isAuthenticated ? (
              <div className="flex items-center space-x-2">
                <Link to="/profile">
                  <Button variant="ghost" size="sm" className="text-ocean-light hover:text-ocean-foam">
                    <User className="h-4 w-4 mr-2" />
                    {user?.name}
                  </Button>
                </Link>
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={logout}
                  className="text-muted-foreground hover:text-destructive"
                >
                  <LogOut className="h-4 w-4" />
                </Button>
              </div>
            ) : (
              <div className="hidden md:flex items-center space-x-2">
                <Link to="/login">
                  <Button variant="ghost" size="sm">Login</Button>
                </Link>
                <Link to="/signup">
                  <Button size="sm" className="wave-animation">Sign Up</Button>
                </Link>
              </div>
            )}

            {/* Mobile Menu */}
            <Sheet open={isOpen} onOpenChange={setIsOpen}>
              <SheetTrigger asChild className="md:hidden">
                <Button variant="ghost" size="sm">
                  <Menu className="h-5 w-5" />
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="w-[300px] sm:w-[400px] ocean-card">
                <div className="flex flex-col space-y-4 mt-8">
                  {filteredNavLinks.map((link) => (
                    <Link
                      key={link.href}
                      to={link.href}
                      onClick={() => setIsOpen(false)}
                      className="text-muted-foreground hover:text-ocean-light transition-colors block py-2"
                    >
                      {link.label}
                    </Link>
                  ))}

                  {!isAuthenticated && (
                    <div className="border-t pt-4 space-y-2">
                      <Link to="/login" onClick={() => setIsOpen(false)}>
                        <Button variant="ghost" className="w-full justify-start">
                          Login
                        </Button>
                      </Link>
                      <Link to="/signup" onClick={() => setIsOpen(false)}>
                        <Button className="w-full wave-animation">
                          Sign Up
                        </Button>
                      </Link>
                    </div>
                  )}
                </div>
              </SheetContent>
            </Sheet>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;