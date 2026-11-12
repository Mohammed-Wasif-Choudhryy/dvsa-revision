def get_labs_html():
    return """
    <!-- MODULE 3: VISUAL INTERACTIVE LABS -->
    <div id="mod-labs" class="space-y-6 hidden">
        <!-- Lab Tabs -->
        <div class="flex flex-wrap gap-2 border-b border-slate-800 pb-3">
            <button onclick="switchLab('stopping')" id="lab-tab-stopping" class="lab-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-amber-500 text-slate-950 shadow">
                🛑 Stopping Distance Calculator
            </button>
            <button onclick="switchLab('studs')" id="lab-tab-studs" class="lab-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
                ✨ Motorway Studs & Smart Gantries
            </button>
            <button onclick="switchLab('speedmatrix')" id="lab-tab-speedmatrix" class="lab-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
                🏎️ Vehicle Class Speed Matrix
            </button>
            <button onclick="switchLab('crossings')" id="lab-tab-crossings" class="lab-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800">
                🚶 Pedestrian Crossing Simulator
            </button>
        </div>

        <!-- LAB 1: STOPPING DISTANCE CALCULATOR -->
        <div id="lab-sec-stopping" class="lab-content-panel space-y-6">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                    <div>
                        <h3 class="text-xl font-bold text-white flex items-center gap-2">
                            <span class="text-amber-400">Lab 1:</span> Stopping Distance & Weather Multiplier Lab
                        </h3>
                        <p class="text-xs text-slate-400">Master the exact Highway Code stopping distances, mental arithmetic shortcuts, and weather multipliers.</p>
                    </div>

                    <!-- Weather Conditions Selector -->
                    <div class="flex items-center gap-2 bg-slate-950 p-1.5 rounded-xl border border-slate-800">
                        <button onclick="setWeather('dry')" id="weather-dry" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 shadow">
                            ☀️ Dry (1x)
                        </button>
                        <button onclick="setWeather('wet')" id="weather-wet" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white">
                            🌧️ Wet (2x)
                        </button>
                        <button onclick="setWeather('ice')" id="weather-ice" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white">
                            ❄️ Ice (10x)
                        </button>
                    </div>
                </div>

                <!-- Speed Selection Buttons -->
                <div class="space-y-2">
                    <label class="text-xs font-mono text-slate-400 block">SELECT VEHICLE SPEED:</label>
                    <div class="grid grid-cols-3 sm:grid-cols-6 gap-2">
                        <button onclick="setStoppingSpeed(20)" id="speed-btn-20" class="speed-selector-btn py-3 px-2 rounded-xl text-center bg-slate-950 hover:bg-slate-800 border border-slate-800 font-mono font-bold text-sm">
                            20 MPH
                        </button>
                        <button onclick="setStoppingSpeed(30)" id="speed-btn-30" class="speed-selector-btn py-3 px-2 rounded-xl text-center bg-amber-500 text-slate-950 font-mono font-bold text-sm shadow">
                            30 MPH
                        </button>
                        <button onclick="setStoppingSpeed(40)" id="speed-btn-40" class="speed-selector-btn py-3 px-2 rounded-xl text-center bg-slate-950 hover:bg-slate-800 border border-slate-800 font-mono font-bold text-sm">
                            40 MPH
                        </button>
                        <button onclick="setStoppingSpeed(50)" id="speed-btn-50" class="speed-selector-btn py-3 px-2 rounded-xl text-center bg-slate-950 hover:bg-slate-800 border border-slate-800 font-mono font-bold text-sm">
                            50 MPH
                        </button>
                        <button onclick="setStoppingSpeed(60)" id="speed-btn-60" class="speed-selector-btn py-3 px-2 rounded-xl text-center bg-slate-950 hover:bg-slate-800 border border-slate-800 font-mono font-bold text-sm">
                            60 MPH
                        </button>
                        <button onclick="setStoppingSpeed(70)" id="speed-btn-70" class="speed-selector-btn py-3 px-2 rounded-xl text-center bg-slate-950 hover:bg-slate-800 border border-slate-800 font-mono font-bold text-sm">
                            70 MPH
                        </button>
                    </div>
                </div>

                <!-- Distance Breakdown Cards -->
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div class="bg-slate-950 p-4 rounded-xl border border-sky-500/30 space-y-1">
                        <span class="text-xs font-mono text-sky-400 font-bold">1. THINKING DISTANCE</span>
                        <div class="text-2xl font-bold font-mono text-white" id="out-thinking-m">9 metres</div>
                        <div class="text-xs text-sky-300 font-mono" id="out-thinking-ft">30 feet</div>
                        <p class="text-[11px] text-slate-400 mt-2">Shortcut: Thinking in feet <strong class="text-white">ALWAYS equals speed in mph</strong>!</p>
                    </div>

                    <div class="bg-slate-950 p-4 rounded-xl border border-rose-500/30 space-y-1">
                        <span class="text-xs font-mono text-rose-400 font-bold">2. BRAKING DISTANCE</span>
                        <div class="text-2xl font-bold font-mono text-white" id="out-braking-m">14 metres</div>
                        <div class="text-xs text-rose-300 font-mono" id="out-braking-ft">45 feet</div>
                        <p class="text-[11px] text-slate-400 mt-2" id="out-braking-formula">Formula: 30 × 1.5 = 45 ft</p>
                    </div>

                    <div class="bg-slate-950 p-4 rounded-xl border border-amber-500/40 bg-amber-500/5 space-y-1">
                        <span class="text-xs font-mono text-amber-400 font-bold">3. TOTAL STOPPING DISTANCE</span>
                        <div class="text-2xl font-bold font-mono text-amber-400" id="out-total-m">23 metres</div>
                        <div class="text-xs text-amber-300 font-mono" id="out-total-ft">75 feet (<span id="out-car-lengths">6</span> car lengths)</div>
                        <p class="text-[11px] text-slate-300 mt-2" id="out-weather-note">Dry road baseline (1 car = 4 metres)</p>
                    </div>
                </div>

                <!-- Visual Bar Comparison -->
                <div class="space-y-2 bg-slate-950 p-4 rounded-xl border border-slate-800">
                    <div class="flex items-center justify-between text-xs text-slate-400 font-mono">
                        <span>VISUAL SCALE PROPORTION:</span>
                        <span id="out-bar-ratio">Thinking: 40% | Braking: 60%</span>
                    </div>
                    <div class="h-6 w-full bg-slate-900 rounded-lg overflow-hidden flex">
                        <div id="bar-thinking" class="bg-sky-500 h-full transition-all duration-300 flex items-center justify-center text-[10px] font-bold text-slate-950" style="width: 40%;">Thinking</div>
                        <div id="bar-braking" class="bg-rose-500 h-full transition-all duration-300 flex items-center justify-center text-[10px] font-bold text-white" style="width: 60%;">Braking</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- LAB 2: MOTORWAY STUDS & SMART GANTRIES -->
        <div id="lab-sec-studs" class="lab-content-panel space-y-6 hidden">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                        <h3 class="text-xl font-bold text-white flex items-center gap-2">
                            <span class="text-emerald-400">Lab 2:</span> Reflective Studs (Cat's Eyes) & Smart Motorways
                        </h3>
                        <p class="text-xs text-slate-400">Click the studs and gantries to inspect their exact exam definitions and active penalties.</p>
                    </div>

                    <div class="flex items-center gap-2">
                        <button onclick="toggleContraflow()" id="btn-contraflow" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700">
                            🚧 Toggle Roadworks Contraflow
                        </button>
                    </div>
                </div>

                <!-- Interactive Motorway Cross-Section Diagram -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800 space-y-4">
                    <div class="grid grid-cols-1 md:grid-cols-5 gap-3 text-center">
                        <!-- Slip Road / Green -->
                        <div onclick="selectStud('green')" class="p-4 rounded-xl border border-slate-800 hover:border-emerald-500/50 bg-slate-900/60 cursor-pointer transition">
                            <div class="w-5 h-5 mx-auto rounded-full bg-emerald-500 stud-green mb-2"></div>
                            <span class="text-xs font-bold text-emerald-400 block">GREEN STUDS</span>
                            <span class="text-[11px] text-slate-400">Slip Road Entry & Exit</span>
                        </div>

                        <!-- Hard Shoulder / Red -->
                        <div onclick="selectStud('red')" class="p-4 rounded-xl border border-slate-800 hover:border-rose-500/50 bg-slate-900/60 cursor-pointer transition">
                            <div class="w-5 h-5 mx-auto rounded-full bg-rose-500 stud-red mb-2"></div>
                            <span class="text-xs font-bold text-rose-400 block">RED STUDS</span>
                            <span class="text-[11px] text-slate-400">Left Edge / Hard Shoulder</span>
                        </div>

                        <!-- Lane Markings / White -->
                        <div onclick="selectStud('white')" class="p-4 rounded-xl border border-slate-800 hover:border-white/50 bg-slate-900/60 cursor-pointer transition">
                            <div class="w-5 h-5 mx-auto rounded-full bg-white stud-white mb-2"></div>
                            <span class="text-xs font-bold text-white block">WHITE STUDS</span>
                            <span class="text-[11px] text-slate-400">Between Running Lanes</span>
                        </div>

                        <!-- Central Reservation / Amber -->
                        <div onclick="selectStud('amber')" class="p-4 rounded-xl border border-slate-800 hover:border-amber-500/50 bg-slate-900/60 cursor-pointer transition">
                            <div class="w-5 h-5 mx-auto rounded-full bg-amber-500 stud-amber mb-2"></div>
                            <span class="text-xs font-bold text-amber-400 block">AMBER STUDS</span>
                            <span class="text-[11px] text-slate-400">Central Reservation (Right)</span>
                        </div>

                        <!-- Contraflow / Fluorescent Green-Yellow -->
                        <div onclick="selectStud('yellow')" class="p-4 rounded-xl border border-slate-800 hover:border-lime-500/50 bg-slate-900/60 cursor-pointer transition">
                            <div class="w-5 h-5 mx-auto rounded-full bg-lime-400 stud-cyanyellow mb-2"></div>
                            <span class="text-xs font-bold text-lime-400 block">FLUORESCENT GREEN</span>
                            <span class="text-[11px] text-slate-400">Contraflow & Roadworks</span>
                        </div>
                    </div>

                    <!-- Detail Card for Selected Stud -->
                    <div id="stud-detail-box" class="p-4 bg-slate-900 rounded-xl border border-slate-800 text-xs space-y-1">
                        <span id="stud-detail-title" class="font-bold text-amber-400 text-sm">Click any stud colour above to view tactical rules.</span>
                        <p id="stud-detail-desc" class="text-slate-400"></p>
                    </div>
                </div>

                <!-- Smart Motorway Overhead Gantry Simulator -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800 space-y-4">
                    <h4 class="text-sm font-bold text-white flex items-center gap-2">
                        <span>🌉</span> Smart Motorway Gantry Simulator (Click Lanes to Toggle Red 'X')
                    </h4>
                    <div class="grid grid-cols-4 gap-3 text-center font-mono">
                        <div onclick="toggleGantryLane(1)" id="gantry-lane-1" class="p-4 rounded-xl border border-slate-800 bg-slate-900 cursor-pointer">
                            <div class="text-2xl font-bold text-emerald-400 mb-1" id="gantry-val-1">60</div>
                            <span class="text-[10px] text-slate-400">LANE 1 (LEFT)</span>
                        </div>
                        <div onclick="toggleGantryLane(2)" id="gantry-lane-2" class="p-4 rounded-xl border border-slate-800 bg-slate-900 cursor-pointer">
                            <div class="text-2xl font-bold text-emerald-400 mb-1" id="gantry-val-2">60</div>
                            <span class="text-[10px] text-slate-400">LANE 2 (MIDDLE)</span>
                        </div>
                        <div onclick="toggleGantryLane(3)" id="gantry-lane-3" class="p-4 rounded-xl border border-slate-800 bg-slate-900 cursor-pointer">
                            <div class="text-2xl font-bold text-red-500 font-black mb-1 animate-pulse" id="gantry-val-3">✕</div>
                            <span class="text-[10px] text-rose-400 font-bold">LANE 3 (CLOSED)</span>
                        </div>
                        <div onclick="toggleGantryLane(4)" id="gantry-lane-4" class="p-4 rounded-xl border border-slate-800 bg-slate-900 cursor-pointer">
                            <div class="text-2xl font-bold text-emerald-400 mb-1" id="gantry-val-4">60</div>
                            <span class="text-[10px] text-slate-400">LANE 4 (RIGHT)</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-400">
                        <strong class="text-rose-400">Red 'X' Rule:</strong> Driving in a lane with a Red 'X' is illegal and monitored by automatic enforcement cameras. Fixed penalty: <strong class="text-white">£100 fine and 3 penalty points</strong>.
                    </p>
                </div>
            </div>
        </div>

        <!-- LAB 3: VEHICLE CLASS SPEED MATRIX LAB -->
        <div id="lab-sec-speedmatrix" class="lab-content-panel space-y-6 hidden">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-sky-400">Lab 3:</span> Interactive Vehicle Class Speed Limit Tester
                    </h3>
                </div>

                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
                    <button onclick="selectVehicleClass('car')" id="vclass-car" class="vclass-btn p-3 rounded-xl text-center bg-amber-500 text-slate-950 font-bold text-xs shadow">
                        🚗 Car / Motorcycle
                    </button>
                    <button onclick="selectVehicleClass('car_derived')" id="vclass-car_derived" class="vclass-btn p-3 rounded-xl text-center bg-slate-950 text-slate-300 hover:bg-slate-800 border border-slate-800 font-semibold text-xs">
                        🚐 Car-Derived Van
                    </button>
                    <button onclick="selectVehicleClass('panel_van')" id="vclass-panel_van" class="vclass-btn p-3 rounded-xl text-center bg-slate-950 text-slate-300 hover:bg-slate-800 border border-slate-800 font-semibold text-xs">
                        🚚 Goods Van (<3.5t)
                    </button>
                    <button onclick="selectVehicleClass('towing')" id="vclass-towing" class="vclass-btn p-3 rounded-xl text-center bg-slate-950 text-slate-300 hover:bg-slate-800 border border-slate-800 font-semibold text-xs">
                        🚙 Towing Trailer
                    </button>
                    <button onclick="selectVehicleClass('hgv')" id="vclass-hgv" class="vclass-btn p-3 rounded-xl text-center bg-slate-950 text-slate-300 hover:bg-slate-800 border border-slate-800 font-semibold text-xs">
                        🚛 HGV (>7.5t)
                    </button>
                    <button onclick="selectVehicleClass('bus')" id="vclass-bus" class="vclass-btn p-3 rounded-xl text-center bg-slate-950 text-slate-300 hover:bg-slate-800 border border-slate-800 font-semibold text-xs">
                        🚌 Bus / Coach (≤12m)
                    </button>
                </div>

                <!-- Active Speed Display -->
                <div class="grid grid-cols-1 sm:grid-cols-4 gap-4 text-center font-mono">
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
                        <span class="text-xs text-slate-400 block mb-1">BUILT-UP AREA</span>
                        <div class="text-3xl font-bold text-amber-400" id="v-speed-builtup">30 MPH</div>
                        <span class="text-[10px] text-slate-500">Streetlights present</span>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
                        <span class="text-xs text-slate-400 block mb-1">SINGLE CARRIAGEWAY</span>
                        <div class="text-3xl font-bold text-emerald-400" id="v-speed-single">60 MPH</div>
                        <span class="text-[10px] text-slate-500">No central barrier</span>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
                        <span class="text-xs text-slate-400 block mb-1">DUAL CARRIAGEWAY</span>
                        <div class="text-3xl font-bold text-emerald-400" id="v-speed-dual">70 MPH</div>
                        <span class="text-[10px] text-slate-500">Divided by reservation</span>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
                        <span class="text-xs text-slate-400 block mb-1">MOTORWAY</span>
                        <div class="text-3xl font-bold text-emerald-400" id="v-speed-motorway">70 MPH</div>
                        <span class="text-[10px] text-slate-500" id="v-speed-mway-note">Full access</span>
                    </div>
                </div>

                <div id="v-restriction-alert" class="p-4 bg-slate-950 rounded-xl border border-slate-800 text-xs text-slate-300">
                    <!-- Dynamic note on right lane ban / weight specifics -->
                </div>
            </div>
        </div>

        <!-- LAB 4: PEDESTRIAN CROSSING SIMULATOR -->
        <div id="lab-sec-crossings" class="lab-content-panel space-y-6 hidden">
            <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-6">
                <h3 class="text-xl font-bold text-white flex items-center gap-2">
                    <span class="text-indigo-400">Lab 4:</span> Pedestrian Crossings & Light Cycles Comparison
                </h3>
                <div class="grid grid-cols-1 md:grid-cols-5 gap-3">
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-amber-400 font-bold text-sm">1. Pelican Crossing</div>
                        <p class="text-xs text-slate-400">Pedestrian Light Controlled. Features a <strong class="text-amber-400">FLASHING AMBER</strong> phase.</p>
                        <div class="p-2 bg-slate-900 rounded text-[11px] text-slate-300">Rule: Give way to pedestrians on crossing. If clear, you may proceed.</div>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-emerald-400 font-bold text-sm">2. Puffin Crossing</div>
                        <p class="text-xs text-slate-400">User-Friendly Intelligent. <strong class="text-rose-400">NO FLASHING AMBER</strong>. Infrared heat sensors on top.</p>
                        <div class="p-2 bg-slate-900 rounded text-[11px] text-slate-300">Rule: Standard light sequence. Lights only change when pedestrians finish crossing.</div>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-sky-400 font-bold text-sm">3. Toucan Crossing</div>
                        <p class="text-xs text-slate-400"><strong class="text-sky-400">"Two-Can" Cross:</strong> Pedestrians AND Cyclists cross together.</p>
                        <div class="p-2 bg-slate-900 rounded text-[11px] text-slate-300">Rule: Cyclists do NOT have to dismount. No flashing amber.</div>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-purple-400 font-bold text-sm">4. Pegasus Crossing</div>
                        <p class="text-xs text-slate-400">For <strong class="text-purple-400">Horse Riders & Equestrians</strong>.</p>
                        <div class="p-2 bg-slate-900 rounded text-[11px] text-slate-300">Rule: Push buttons are mounted higher up for mounted riders.</div>
                    </div>
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="text-rose-400 font-bold text-sm">5. Zebra Crossing</div>
                        <p class="text-xs text-slate-400">Flashing yellow <strong class="text-amber-400">Belisha beacons</strong> on black/white striped poles.</p>
                        <div class="p-2 bg-slate-900 rounded text-[11px] text-slate-300">Rule: MUST give way once a pedestrian steps onto the crossing. White zig-zags forbid parking/overtaking.</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

print("Module 3 generator ready.")
