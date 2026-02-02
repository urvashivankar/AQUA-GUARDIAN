import React from 'react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { User, Shield, Building, MapPin, Camera, CheckCircle, Megaphone, BarChart3, Users } from 'lucide-react';

const HowToUse = () => {
    return (
        <div className="min-h-screen pt-20 pb-12 px-4 bg-gradient-to-b from-background to-muted/20">
            <div className="max-w-5xl mx-auto space-y-8">
                <div className="text-center space-y-4">
                    <h1 className="text-4xl font-bold tracking-tight text-primary">How to Use AQUA Guardian</h1>
                    <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
                        A guide to protecting our water bodies, tailored for every role in our ecosystem.
                    </p>
                </div>

                <Tabs defaultValue="citizen" className="w-full">
                    <TabsList className="grid w-full grid-cols-3 h-16 bg-muted/50 p-1">
                        <TabsTrigger value="citizen" className="gap-2 text-lg">
                            <User className="h-5 w-5" /> Citizen
                        </TabsTrigger>
                        <TabsTrigger value="ngo" className="gap-2 text-lg">
                            <Shield className="h-5 w-5" /> NGO
                        </TabsTrigger>
                        <TabsTrigger value="government" className="gap-2 text-lg">
                            <Building className="h-5 w-5" /> Government
                        </TabsTrigger>
                    </TabsList>

                    {/* Citizen Guide */}
                    <TabsContent value="citizen" className="mt-8 space-y-6 animate-in fade-in-50 duration-500">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <Card className="ocean-card overflow-hidden">
                                <CardHeader className="bg-primary/5">
                                    <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4">
                                        <Camera className="h-6 w-6" />
                                    </div>
                                    <CardTitle>Report Pollution</CardTitle>
                                    <CardDescription>The first step to cleaner water.</CardDescription>
                                </CardHeader>
                                <CardContent className="pt-6 space-y-4">
                                    <ul className="space-y-3">
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-success/10 text-success flex items-center justify-center text-xs font-bold flex-shrink-0">1</div>
                                            <p className="text-sm">Click <strong>'Report Pollution'</strong> and upload a clear photo of the incident.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-success/10 text-success flex items-center justify-center text-xs font-bold flex-shrink-0">2</div>
                                            <p className="text-sm">Allow GPS location access for precise mapping of the incident.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-success/10 text-success flex items-center justify-center text-xs font-bold flex-shrink-0">3</div>
                                            <p className="text-sm">Our AI will instantly analyze the severity and type of pollution.</p>
                                        </li>
                                    </ul>
                                </CardContent>
                            </Card>

                            <Card className="ocean-card overflow-hidden">
                                <CardHeader className="bg-primary/5">
                                    <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4">
                                        <Users className="h-6 w-6" />
                                    </div>
                                    <CardTitle>Take Action</CardTitle>
                                    <CardDescription>Join the community on the ground.</CardDescription>
                                </CardHeader>
                                <CardContent className="pt-6 space-y-4">
                                    <ul className="space-y-3">
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-success/10 text-success flex items-center justify-center text-xs font-bold flex-shrink-0">1</div>
                                            <p className="text-sm">Browse active <strong>'Community Actions'</strong> near you.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-success/10 text-success flex items-center justify-center text-xs font-bold flex-shrink-0">2</div>
                                            <p className="text-sm">Sign up for cleanup drives organized by verified NGOs.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-success/10 text-success flex items-center justify-center text-xs font-bold flex-shrink-0">3</div>
                                            <p className="text-sm">Earn your place on the <strong>'Leaderboard'</strong> through active participation.</p>
                                        </li>
                                    </ul>
                                </CardContent>
                            </Card>
                        </div>
                    </TabsContent>

                    {/* NGO Guide */}
                    <TabsContent value="ngo" className="mt-8 space-y-6 animate-in fade-in-50 duration-500">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <Card className="ocean-card overflow-hidden">
                                <CardHeader className="bg-primary/5">
                                    <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4">
                                        <CheckCircle className="h-6 w-6" />
                                    </div>
                                    <CardTitle>Verify & Validate</CardTitle>
                                    <CardDescription>Bridge the gap between reports and action.</CardDescription>
                                </CardHeader>
                                <CardContent className="pt-6 space-y-4">
                                    <ul className="space-y-3">
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold flex-shrink-0">1</div>
                                            <p className="text-sm">Use your <strong>'Dashboard'</strong> to see pending citizen reports in your area.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold flex-shrink-0">2</div>
                                            <p className="text-sm">Verify the AI analysis and mark reports as 'Actionable'.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold flex-shrink-0">3</div>
                                            <p className="text-sm">Upload "After" photos once cleanups are complete to earn platform trust.</p>
                                        </li>
                                    </ul>
                                </CardContent>
                            </Card>

                            <Card className="ocean-card overflow-hidden">
                                <CardHeader className="bg-primary/5">
                                    <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4">
                                        <Megaphone className="h-6 w-6" />
                                    </div>
                                    <CardTitle>Launch Campaigns</CardTitle>
                                    <CardDescription>Mobilize the local community.</CardDescription>
                                </CardHeader>
                                <CardContent className="pt-6 space-y-4">
                                    <ul className="space-y-3">
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold flex-shrink-0">1</div>
                                            <p className="text-sm">Convert high-severity reports into official <strong>Cleanup Campaigns</strong>.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold flex-shrink-0">2</div>
                                            <p className="text-sm">Manage volunteer registrations and coordinate logistics.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-xs font-bold flex-shrink-0">3</div>
                                            <p className="text-sm">Post <strong>'Success Stories'</strong> to inspire more involvement.</p>
                                        </li>
                                    </ul>
                                </CardContent>
                            </Card>
                        </div>
                    </TabsContent>

                    {/* Government Guide */}
                    <TabsContent value="government" className="mt-8 space-y-6 animate-in fade-in-50 duration-500">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <Card className="ocean-card overflow-hidden">
                                <CardHeader className="bg-primary/5">
                                    <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4">
                                        <BarChart3 className="h-6 w-6" />
                                    </div>
                                    <CardTitle>Data Command Center</CardTitle>
                                    <CardDescription>Strategic oversight of water health.</CardDescription>
                                </CardHeader>
                                <CardContent className="pt-6 space-y-4">
                                    <ul className="space-y-3">
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-blue-500/10 text-blue-500 flex items-center justify-center text-xs font-bold flex-shrink-0">1</div>
                                            <p className="text-sm">Access real-time <strong>Pollution Heatmaps</strong> across your jurisdiction.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-blue-500/10 text-blue-500 flex items-center justify-center text-xs font-bold flex-shrink-0">2</div>
                                            <p className="text-sm">Monitor Key Performance Indicators (KPIs) for resolution rates.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-blue-500/10 text-blue-500 flex items-center justify-center text-xs font-bold flex-shrink-0">3</div>
                                            <p className="text-sm">Audit NGO cleanup proofs to ensure government standards are met.</p>
                                        </li>
                                    </ul>
                                </CardContent>
                            </Card>

                            <Card className="ocean-card overflow-hidden">
                                <CardHeader className="bg-primary/5">
                                    <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary mb-4">
                                        <MapPin className="h-6 w-6" />
                                    </div>
                                    <CardTitle>Dispatch & Resolve</CardTitle>
                                    <CardDescription>Turn data into immediate action.</CardDescription>
                                </CardHeader>
                                <CardContent className="pt-6 space-y-4">
                                    <ul className="space-y-3">
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-blue-500/10 text-blue-500 flex items-center justify-center text-xs font-bold flex-shrink-0">1</div>
                                            <p className="text-sm">Dispatch official municipal cleaning crews for critical severity reports.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-blue-500/10 text-blue-500 flex items-center justify-center text-xs font-bold flex-shrink-0">2</div>
                                            <p className="text-sm">Update resolution status directly on the portal for public visibility.</p>
                                        </li>
                                        <li className="flex gap-3">
                                            <div className="h-6 w-6 rounded-full bg-blue-500/10 text-blue-500 flex items-center justify-center text-xs font-bold flex-shrink-0">3</div>
                                            <p className="text-sm">Collaborate with local NGOs on large-scale marine restoration projects.</p>
                                        </li>
                                    </ul>
                                </CardContent>
                            </Card>
                        </div>
                    </TabsContent>
                </Tabs>

            </div>
        </div>
    );
};

export default HowToUse;
