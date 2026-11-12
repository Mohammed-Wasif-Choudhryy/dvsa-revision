# Generator for Module 1: Academy HTML & Content
def get_academy_html():
    return """
    <!-- MODULE 1: DEEP-DIVE ACADEMY -->
    <div id="mod-academy" class="space-y-6">
        <!-- Sub-navigation for Academy -->
        <div class="flex flex-wrap gap-2 border-b border-slate-800 pb-3">
            <button onclick="switchAcademyTab('signs')" id="acad-tab-signs" class="acad-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-amber-500 text-slate-950 shadow">
                🚦 Obscure Signs & Kerb Markings
            </button>
            <button onclick="switchAcademyTab('mechanics')" id="acad-tab-mechanics" class="acad-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
                🔧 Mechanics, Towing & Tyres
            </button>
            <button onclick="switchAcademyTab('breakdowns')" id="acad-tab-breakdowns" class="acad-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
                🩹 First Aid & Breakdowns
            </button>
            <button onclick="switchAcademyTab('legal')" id="acad-tab-legal" class="acad-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
                ⚖️ Legal Limits & Documentation
            </button>
            <button onclick="switchAcademyTab('speedlimits')" id="acad-tab-speedlimits" class="acad-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
                🏎️ Speed Limits Matrix
            </button>
        </div>

        <!-- SUB-SECTION A: SIGNS & MARKINGS -->
        <div id="acad-sec-signs" class="acad-content-panel space-y-6">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800">
                <div class="flex items-center justify-between mb-4">
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-amber-400">Section A:</span> Obscure Highway Code Signs & Visual Traps
                    </h3>
                    <span class="text-xs bg-amber-500/10 text-amber-400 border border-amber-500/30 px-2.5 py-1 rounded-full font-mono">High-Fail Traps</span>
                </div>
                <p class="text-sm text-slate-400 mb-6">
                    Practical drivers fail signs because UK road signs follow strict syntactic rules that are easy to confuse under exam pressure. Memorise the core grammar: <strong class="text-white">Red Circle = Must Not (Prohibition)</strong>, <strong class="text-white">Blue Circle = Must Do (Mandatory Command)</strong>, <strong class="text-white">Triangle = Warning (Hazard Ahead)</strong>, <strong class="text-white">Rectangle = Information / Direction</strong>.
                </p>

                <!-- Grid of Sign Cards -->
                <div id="academy-signs-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    <!-- Populated via JavaScript with SVG cards -->
                </div>
            </div>

            <!-- Road Markings & Kerb Traps -->
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-4">
                <h4 class="text-lg font-bold text-white flex items-center gap-2">
                    <span class="text-sky-400">Kerb & Road Markings Master Decoder:</span> The Lines Practical Drivers Get Wrong
                </h4>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80">
                        <div class="h-2 w-full bg-amber-400 rounded-full mb-3"></div>
                        <h5 class="font-bold text-white text-sm mb-1">Single Yellow Line</h5>
                        <p class="text-slate-400">No waiting during the operational hours displayed on the accompanying roadside time plate. Parking permitted outside those hours.</p>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80">
                        <div class="h-2 w-full bg-amber-400 rounded-full mb-1"></div>
                        <div class="h-2 w-full bg-amber-400 rounded-full mb-3"></div>
                        <h5 class="font-bold text-white text-sm mb-1">Double Yellow Lines</h5>
                        <p class="text-slate-400"><strong class="text-amber-400">No waiting at ANY time.</strong> No sign required. You may stop briefly only to set down/pick up passengers unless loading restrictions apply.</p>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80">
                        <div class="flex gap-1 mb-3">
                            <div class="h-4 w-2 bg-amber-400 rounded-sm"></div>
                        </div>
                        <h5 class="font-bold text-white text-sm mb-1">Single Kerb Loading Blip</h5>
                        <p class="text-slate-400"><strong class="text-rose-400">No loading or unloading</strong> during the times shown on the accompanying white plate. Check plate carefully.</p>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80">
                        <div class="flex gap-1 mb-3">
                            <div class="h-4 w-2 bg-amber-400 rounded-sm"></div>
                            <div class="h-4 w-2 bg-amber-400 rounded-sm"></div>
                        </div>
                        <h5 class="font-bold text-white text-sm mb-1">Double Kerb Loading Blips</h5>
                        <p class="text-slate-400"><strong class="text-rose-400">Strictly NO loading or unloading at ANY time.</strong> Even commercial delivery vans cannot stop.</p>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs pt-2">
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
                        <span class="font-mono text-emerald-400 font-bold block mb-1">BOX JUNCTIONS (Rule 174)</span>
                        <p class="text-slate-400">Do not enter the box unless your exit road is clear. <strong class="text-white">THE EXCEPTION:</strong> You may enter and wait if turning right and only prevented by oncoming traffic.</p>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
                        <span class="font-mono text-rose-400 font-bold block mb-1">WHITE ZIG-ZAGS (Rule 191)</span>
                        <p class="text-slate-400">Painted approaching Zebra, Pelican, Puffin & Toucan crossings. <strong class="text-white">Strictly NO parking</strong> and <strong class="text-rose-400">NO overtaking</strong> the lead moving or stationary vehicle.</p>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
                        <span class="font-mono text-amber-400 font-bold block mb-1">HATCHED CHEVRONS (Rule 130)</span>
                        <p class="text-slate-400">If bordered by a <strong class="text-white">broken white line</strong>: do not enter unless safe. If bordered by a <strong class="text-rose-400">solid white line</strong>: you MUST NOT enter except in an emergency.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SUB-SECTION B: MECHANICS, TOWING & TYRES -->
        <div id="acad-sec-mechanics" class="acad-content-panel space-y-6 hidden">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-emerald-400">Section B:</span> Vehicle Mechanics, Towing & Safety Systems
                    </h3>
                    <span class="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-2.5 py-1 rounded-full font-mono">High-Yield Technical</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <!-- DPF & Cat -->
                    <div class="bg-slate-950 p-5 rounded-xl border border-slate-800 space-y-3">
                        <div class="flex items-center gap-2 text-amber-400 font-bold text-sm">
                            <span class="text-lg">⚠️</span> DPF & Catalytic Converter
                        </div>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            <strong class="text-white">DPF Regeneration:</strong> Diesel Particulate Filters trap soot. When the DPF warning light illuminates, drive at sustained high speed (40–50+ mph) on a dual carriageway/motorway for 20–30 minutes to generate exhaust heat.
                        </p>
                        <p class="text-xs text-rose-400 leading-relaxed font-semibold">
                            PROHIBITION: Never push-start or tow-start a petrol car with a catalytic converter. Unburnt fuel enters the catalyst, ignites, and permanently melts the ceramic core.
                        </p>
                    </div>

                    <!-- Caravan Snaking & Towing -->
                    <div class="bg-slate-950 p-5 rounded-xl border border-slate-800 space-y-3">
                        <div class="flex items-center gap-2 text-sky-400 font-bold text-sm">
                            <span class="text-lg">🚐</span> Caravan Snaking & Cables
                        </div>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            <strong class="text-white">Snaking Physics:</strong> Caused by crosswinds, passing HGVs, or incorrect noseweight. <strong class="text-emerald-400">Counteraction:</strong> Ease gently off the accelerator and hold the steering straight. <span class="text-rose-400 font-semibold">NEVER brake hard or counter-steer</span>, which causes immediate jackknifing.
                        </p>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            <strong class="text-white">Breakaway Cable:</strong> Thin steel cable clipped between trailer brake and towbar. If trailer detaches, it pulls the trailer handbrake ON before snapping.
                        </p>
                        <p class="text-xs text-amber-300 font-mono">
                            Max trailer width: 2.55m | Max length: 7.0m
                        </p>
                    </div>

                    <!-- Tyres, Blowouts & Brakes -->
                    <div class="bg-slate-950 p-5 rounded-xl border border-slate-800 space-y-3">
                        <div class="flex items-center gap-2 text-indigo-400 font-bold text-sm">
                            <span class="text-lg">🛞</span> Tyres, Blowouts & Brakes
                        </div>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            <strong class="text-white">Legal Tread:</strong> 1.6 mm across the central 3/4 breadth and around the entire circumference. Check pressures when <strong class="text-white">COLD</strong> (driving heats air, giving false high readings). Increase pressures for heavy loads or high-speed driving.
                        </p>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            <strong class="text-white">Front Blowout:</strong> Car pulls violently to the side of the burst tyre. Grip wheel firmly, ease off gas. <strong class="text-white">Rear Blowout:</strong> Rear end fishtails.
                        </p>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            <strong class="text-white">Brake Fade:</strong> Overheating brake pads on steep downhill descents. Remedy: shift down to a lower gear to utilise <strong class="text-emerald-400">engine braking</strong>.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- SUB-SECTION C: FIRST AID & BREAKDOWNS -->
        <div id="acad-sec-breakdowns" class="acad-content-panel space-y-6 hidden">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-rose-400">Section C:</span> Emergency Protocols, First Aid & Breakdowns
                    </h3>
                    <span class="text-xs bg-rose-500/10 text-rose-400 border border-rose-500/30 px-2.5 py-1 rounded-full font-mono">Exam Mandatory</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    <!-- DR ABC -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-rose-400 font-bold text-sm">DR ABC Sequence</div>
                        <ul class="space-y-1 text-slate-400">
                            <li><strong class="text-white">D - Danger:</strong> Check for safe approach first.</li>
                            <li><strong class="text-white">R - Response:</strong> Shake shoulders, ask loudly.</li>
                            <li><strong class="text-white">A - Airway:</strong> Tilt head back, lift chin.</li>
                            <li><strong class="text-white">B - Breathing:</strong> Look/listen for up to 10s.</li>
                            <li><strong class="text-white">C - Circulation:</strong> Control severe bleeding.</li>
                        </ul>
                    </div>

                    <!-- CPR Numbers -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-amber-400 font-bold text-sm">CPR Exact Numbers</div>
                        <p class="text-slate-400"><strong class="text-white">Adult Depth:</strong> 5 to 6 cm compressions.</p>
                        <p class="text-slate-400"><strong class="text-white">Compression Rate:</strong> 100 to 120 per minute (rhythm of 'Stayin Alive').</p>
                        <p class="text-slate-400"><strong class="text-white">Ratio:</strong> 30 compressions to 2 rescue breaths (or hands-only CPR).</p>
                    </div>

                    <!-- Burns & Bleeding -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-sky-400 font-bold text-sm">Burns & Helmets</div>
                        <p class="text-slate-400"><strong class="text-white">Burns:</strong> Cool with clean, cold water for <strong class="text-amber-400">AT LEAST 20 MINUTES</strong>. Never remove clothing stuck to burns.</p>
                        <p class="text-slate-400"><strong class="text-white">Motorcyclist Helmet:</strong> <strong class="text-rose-400">NEVER REMOVE</strong> unless airway is blocked or they are not breathing.</p>
                    </div>

                    <!-- Warning Triangle & Smart Motorways -->
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-indigo-400 font-bold text-sm">Warning Triangle & SOS</div>
                        <p class="text-slate-400"><strong class="text-white">Triangle:</strong> Place at least <strong class="text-amber-400">45 metres (147 ft)</strong> behind vehicle. <strong class="text-rose-400">NEVER ON A MOTORWAY.</strong></p>
                        <p class="text-slate-400"><strong class="text-white">Smart Motorway SOS:</strong> Emergency areas every 1.5 miles. Face oncoming traffic when using phone. Walk up verge behind barrier.</p>
                    </div>
                </div>

                <!-- Level Crossing Breakdown 1-2-3 Rule -->
                <div class="bg-slate-950 p-4 rounded-xl border border-amber-500/30 bg-amber-500/5">
                    <h5 class="text-sm font-bold text-amber-400 mb-2 flex items-center gap-2">
                        <span>🚆</span> Level Crossing Breakdown: The Strict 1-2-3 Rule
                    </h5>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs text-slate-300">
                        <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
                            <span class="font-bold text-amber-400 block mb-1">Step 1: Immediate Evacuation</span>
                            Get all passengers OUT of the vehicle and completely clear of the tracks immediately.
                        </div>
                        <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
                            <span class="font-bold text-amber-400 block mb-1">Step 2: Railway Telephone</span>
                            Use the dedicated railway phone next to the barrier to alert the signalman.
                        </div>
                        <div class="p-2.5 bg-slate-900 rounded-lg border border-slate-800">
                            <span class="font-bold text-amber-400 block mb-1">Step 3: Move Only If Told</span>
                            Only attempt to move the car if instructed by the signalman, and ensure you close gates behind you.
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SUB-SECTION D: LEGAL LIMITS & DOCUMENTATION -->
        <div id="acad-sec-legal" class="acad-content-panel space-y-6 hidden">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-purple-400">Section D:</span> Statutory Thresholds, Penalties & Licensing
                    </h3>
                    <span class="text-xs bg-purple-500/10 text-purple-400 border border-purple-500/30 px-2.5 py-1 rounded-full font-mono">Numbers to Memorise</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Alcohol Comparison Table -->
                    <div class="bg-slate-950 p-5 rounded-xl border border-slate-800 space-y-3">
                        <h4 class="font-bold text-white text-sm flex items-center gap-2">
                            <span>🍺</span> Alcohol Limits: England/Wales vs Scotland
                        </h4>
                        <table class="w-full text-xs text-left">
                            <thead>
                                <tr class="text-slate-400 border-b border-slate-800">
                                    <th class="pb-2">Test Type</th>
                                    <th class="pb-2 text-amber-400 font-bold">England, Wales & NI</th>
                                    <th class="pb-2 text-rose-400 font-bold">Scotland (Stricter)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800/60 font-mono">
                                <tr>
                                    <td class="py-2 text-slate-300">Breath (mcg/100ml)</td>
                                    <td class="py-2 text-amber-400 font-bold">35 mcg</td>
                                    <td class="py-2 text-rose-400 font-bold">22 mcg</td>
                                </tr>
                                <tr>
                                    <td class="py-2 text-slate-300">Blood (mg/100ml)</td>
                                    <td class="py-2 text-amber-400 font-bold">80 mg</td>
                                    <td class="py-2 text-rose-400 font-bold">50 mg</td>
                                </tr>
                                <tr>
                                    <td class="py-2 text-slate-300">Urine (mg/100ml)</td>
                                    <td class="py-2 text-amber-400 font-bold">107 mg</td>
                                    <td class="py-2 text-rose-400 font-bold">67 mg</td>
                                </tr>
                            </tbody>
                        </table>
                        <p class="text-xs text-slate-400">
                            Scotland reduced its legal limit in 2014 to align closer with European norms. Memorise the breath pair: <strong class="text-white">35 vs 22 mcg</strong>!
                        </p>
                    </div>

                    <!-- Penalties & Documentation -->
                    <div class="bg-slate-950 p-5 rounded-xl border border-slate-800 space-y-3 text-xs">
                        <h4 class="font-bold text-white text-sm flex items-center gap-2">
                            <span>📄</span> Key Statutory Deadlines & Rules
                        </h4>
                        <div class="space-y-2 text-slate-400">
                            <p><strong class="text-white">New Drivers Act (Probation):</strong> 6 penalty points within 2 years of passing practical test = <strong class="text-rose-400">Automatic licence revocation</strong>. Must retake BOTH theory and practical tests.</p>
                            <p><strong class="text-white">Collision Reporting:</strong> Must report to police in person as soon as practicable and within <strong class="text-amber-400">24 HOURS</strong> if insurance/contact details were not exchanged.</p>
                            <p><strong class="text-white">HO/RT1 Document Production:</strong> <strong class="text-amber-400">7 DAYS</strong> to present licence, insurance, or MOT at a chosen police station if requested.</p>
                            <p><strong class="text-white">MOT & SORN:</strong> First MOT at <strong class="text-amber-400">3 years old</strong>, then annually. SORN (Statutory Off Road Notification) is valid <strong class="text-emerald-400">INDEFINITELY</strong> until taxed or scrapped.</p>
                            <p><strong class="text-white">Horn Curfew:</strong> Illegal between <strong class="text-amber-400">11:30 pm and 7:00 am</strong> in built-up areas.</p>
                            <p><strong class="text-white">Night Parking:</strong> On roads >30 mph, you MUST leave parking lights (sidelights) on and park facing the direction of traffic on the left.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- SUB-SECTION E: SPEED LIMITS MATRIX -->
        <div id="acad-sec-speedlimits" class="acad-content-panel space-y-6 hidden">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-amber-400">Section E:</span> National Speed Limits by Vehicle Class Matrix
                    </h3>
                    <span class="text-xs bg-amber-500/10 text-amber-400 border border-amber-500/30 px-2.5 py-1 rounded-full font-mono">The Trap Matrix</span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-950 text-slate-300 border-b border-slate-800 font-bold">
                                <th class="p-3">Vehicle Category</th>
                                <th class="p-3 text-center">Built-Up Area</th>
                                <th class="p-3 text-center">Single Carriageway</th>
                                <th class="p-3 text-center">Dual Carriageway</th>
                                <th class="p-3 text-center">Motorway</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800 text-slate-300 font-mono">
                            <tr class="hover:bg-slate-800/40">
                                <td class="p-3 font-sans font-semibold text-white">Cars, Motorcycles & Car-Derived Vans (<2t max laden)</td>
                                <td class="p-3 text-center">30 mph</td>
                                <td class="p-3 text-center text-emerald-400 font-bold">60 mph</td>
                                <td class="p-3 text-center text-emerald-400 font-bold">70 mph</td>
                                <td class="p-3 text-center text-emerald-400 font-bold">70 mph</td>
                            </tr>
                            <tr class="hover:bg-slate-800/40 bg-slate-950/40">
                                <td class="p-3 font-sans font-semibold text-amber-400">Standard Goods Vans (e.g. Ford Transit, <3.5t)</td>
                                <td class="p-3 text-center">30 mph</td>
                                <td class="p-3 text-center text-rose-400 font-bold">50 mph ⚠️</td>
                                <td class="p-3 text-center text-rose-400 font-bold">60 mph ⚠️</td>
                                <td class="p-3 text-center text-emerald-400 font-bold">70 mph</td>
                            </tr>
                            <tr class="hover:bg-slate-800/40">
                                <td class="p-3 font-sans font-semibold text-sky-400">Cars Towing Caravans or Trailers</td>
                                <td class="p-3 text-center">30 mph</td>
                                <td class="p-3 text-center text-rose-400 font-bold">50 mph ⚠️</td>
                                <td class="p-3 text-center text-rose-400 font-bold">60 mph ⚠️</td>
                                <td class="p-3 text-center text-rose-400 font-bold">60 mph ⚠️*</td>
                            </tr>
                            <tr class="hover:bg-slate-800/40 bg-slate-950/40">
                                <td class="p-3 font-sans font-semibold text-purple-400">Goods Vehicles (>7.5t in England & Wales)</td>
                                <td class="p-3 text-center">30 mph</td>
                                <td class="p-3 text-center text-rose-400 font-bold">50 mph</td>
                                <td class="p-3 text-center text-rose-400 font-bold">60 mph</td>
                                <td class="p-3 text-center text-rose-400 font-bold">60 mph*</td>
                            </tr>
                            <tr class="hover:bg-slate-800/40">
                                <td class="p-3 font-sans font-semibold text-indigo-400">Buses, Coaches & Minibuses (≤12m length)</td>
                                <td class="p-3 text-center">30 mph</td>
                                <td class="p-3 text-center text-rose-400 font-bold">50 mph</td>
                                <td class="p-3 text-center text-rose-400 font-bold">60 mph</td>
                                <td class="p-3 text-center text-emerald-400 font-bold">70 mph</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <p class="text-xs text-slate-400">
                    <strong class="text-rose-400">*Right-hand lane prohibition:</strong> Vehicles towing trailers and goods vehicles over 7.5 tonnes are <strong class="text-white">banned from using the outside (right-hand) lane</strong> of a motorway with three or more lanes!
                </p>
            </div>
        </div>
    </div>
    """

print("Module 1 generator ready.")
