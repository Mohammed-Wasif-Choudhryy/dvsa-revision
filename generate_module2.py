def get_hazard_html():
    return """
    <!-- MODULE 2: 3D COCKPIT HAZARD PERCEPTION SIMULATOR -->
    <div id="mod-hazard" class="space-y-6 hidden">
        <!-- Scenario Selector & Mode Bar -->
        <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 space-y-3">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
                <div>
                    <h3 class="text-lg font-bold text-white flex items-center gap-2">
                        <span class="text-rose-400">DVSA 3D Cockpit Hazard Perception Simulator</span>
                        <span class="text-xs bg-rose-500/10 text-rose-400 border border-rose-500/30 px-2 py-0.5 rounded-full font-mono">Realistic Perspective</span>
                    </h3>
                    <p class="text-xs text-slate-400">First-person UK driver perspective (driving on the LEFT). Practice the 3-Click Pulse without triggering anti-cheat.</p>
                </div>

                <div class="flex items-center gap-2 flex-wrap">
                    <!-- Mode Toggle -->
                    <div class="bg-slate-950 p-1 rounded-xl border border-slate-800 flex items-center text-xs">
                        <button onclick="setHPMode('practice')" id="hp-mode-practice" class="px-3 py-1.5 rounded-lg font-semibold bg-amber-500 text-slate-950 shadow">
                            🎯 Practice & Coach
                        </button>
                        <button onclick="setHPMode('exam')" id="hp-mode-exam" class="px-3 py-1.5 rounded-lg font-semibold text-slate-400 hover:text-white">
                            ⏱️ DVSA Exam Mode
                        </button>
                    </div>

                    <!-- Audio Sound Toggle -->
                    <button onclick="toggleHPSound()" id="hp-sound-btn" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl text-xs font-semibold border border-slate-700 flex items-center gap-1.5">
                        <span id="hp-sound-icon">🔊</span> Sound: ON
                    </button>
                </div>
            </div>

            <!-- Scenarios Carousel / Buttons -->
            <div id="hp-scenario-buttons" class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-1.5 pt-1">
                <!-- Dynamically populated with scenario tabs -->
            </div>
        </div>

        <!-- Cockpit Canvas Simulator Viewport -->
        <div class="bg-slate-950 rounded-2xl border border-slate-800 p-4 space-y-3 shadow-2xl">
            <!-- Top HUD Bar -->
            <div class="flex items-center justify-between text-xs font-mono bg-slate-900/90 px-4 py-2.5 rounded-xl border border-slate-800">
                <div class="flex items-center gap-2">
                    <span id="hp-status-dot" class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span id="hp-scenario-title" class="font-bold text-white text-sm">1. Zebra Crossing Step-Out</span>
                    <span id="hp-scenario-env" class="hidden sm:inline bg-slate-800 text-slate-300 px-2 py-0.5 rounded text-[11px]">Urban 30 mph</span>
                </div>
                <div class="flex items-center gap-4">
                    <div class="flex items-center gap-1 text-slate-400">
                        <span>TIME:</span>
                        <span id="hp-timer" class="text-white font-bold text-sm">0.0s / 18.0s</span>
                    </div>
                    <div class="flex items-center gap-1 text-slate-400">
                        <span>CLICKS:</span>
                        <span id="hp-click-count" class="text-amber-400 font-bold text-sm">0</span>
                        <span class="text-slate-600">/ 10 max</span>
                    </div>
                </div>
            </div>

            <!-- Real-Time Practice Coach Banner (visible only in Practice Mode) -->
            <div id="hp-live-coach-banner" class="bg-slate-900 px-4 py-2 rounded-xl border border-amber-500/30 flex items-center justify-between text-xs">
                <div class="flex items-center gap-2">
                    <span id="hp-phase-badge" class="px-2 py-0.5 rounded font-mono font-bold bg-slate-800 text-slate-400">PHASE: STATIC CLUE</span>
                    <span id="hp-phase-hint" class="text-slate-300">Pedestrian on pavement. Look ahead and prepare.</span>
                </div>
                <div id="hp-window-indicator" class="hidden font-mono font-bold text-emerald-400 flex items-center gap-1 animate-pulse">
                    <span>⚡ SCORING WINDOW OPEN:</span>
                    <span id="hp-current-pts" class="text-sm bg-emerald-500/20 px-2 py-0.5 rounded border border-emerald-500/40">5 PTS</span>
                </div>
            </div>

            <!-- The 3D Canvas Box -->
            <div class="relative w-full aspect-video max-h-[500px] rounded-xl overflow-hidden bg-black border border-slate-800 select-none cursor-crosshair">
                <canvas id="hp-canvas" width="960" height="540" class="w-full h-full block" onclick="recordHazardClick()"></canvas>

                <!-- Anti-Cheat Overlay (Real DVSA Modal) -->
                <div id="hp-anticheat-overlay" class="absolute inset-0 bg-red-950/90 backdrop-blur-sm z-30 hidden flex flex-col items-center justify-center p-6 text-center space-y-4">
                    <div class="w-16 h-16 rounded-full bg-red-600/20 border-2 border-red-500 flex items-center justify-center text-3xl animate-bounce">
                        ⚠️
                    </div>
                    <div>
                        <h4 class="text-xl font-bold text-white tracking-wide">DVSA ANTI-CHEAT TRIGGERED</h4>
                        <p class="text-sm text-red-200 mt-1 max-w-md">An irregular, rhythmic, or spam clicking pattern was detected by the test algorithm.</p>
                        <p id="hp-anticheat-reason" class="text-xs text-amber-300 font-mono mt-2 bg-red-900/60 py-1 px-3 rounded-lg border border-red-700/50 inline-block"></p>
                    </div>
                    <div class="text-3xl font-black font-mono text-red-400">SCORE FOR THIS CLIP: 0 / 5</div>
                    <button onclick="resetHazardScenario()" class="px-6 py-2.5 bg-red-600 hover:bg-red-500 text-white font-bold text-xs rounded-xl shadow-lg transition">
                        Restart Scenario
                    </button>
                </div>

                <!-- Click Ripple Overlay Effect -->
                <div id="hp-click-flash" class="absolute inset-0 pointer-events-none transition-opacity duration-150 opacity-0 bg-white/10"></div>
            </div>

            <!-- Bottom DVSA Timeline & Flags Bar -->
            <div class="space-y-2 bg-slate-900/80 p-3 rounded-xl border border-slate-800">
                <div class="flex items-center justify-between text-xs text-slate-400 font-mono">
                    <span>TIMELINE & DVSA CHEVRON FLAGS:</span>
                    <span class="text-[11px] text-slate-500">Click anywhere on canvas or press <kbd class="px-1.5 py-0.5 bg-slate-800 text-slate-200 rounded border border-slate-700 font-mono">SPACE</kbd></span>
                </div>

                <!-- The Timeline Track -->
                <div class="relative h-9 bg-slate-950 rounded-lg border border-slate-800 overflow-hidden cursor-pointer" id="hp-timeline-track" onclick="scrubTimeline(event)">
                    <!-- Scoring Window Highlight (Green to Yellow gradient) -->
                    <div id="hp-window-layer" class="absolute top-0 bottom-0 bg-emerald-500/20 border-l border-r border-emerald-400/60 hidden transition-all"></div>
                    
                    <!-- Playhead -->
                    <div id="hp-playhead" class="absolute top-0 bottom-0 w-1 bg-amber-400 z-10 pointer-events-none transition-all shadow-[0_0_8px_rgba(245,158,11,1)]" style="left: 0%;"></div>
                    
                    <!-- Chevrons / Flags Layer -->
                    <div id="hp-flags-layer" class="absolute inset-0 pointer-events-none"></div>
                </div>

                <!-- Interactive Scrubber & Controls Bar -->
                <div class="flex items-center justify-between pt-2 gap-2 flex-wrap text-xs">
                    <div class="flex items-center gap-2">
                        <button onclick="toggleHazardPlay()" id="hp-play-btn" class="px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl flex items-center gap-1.5 shadow">
                            <span id="hp-play-icon">▶</span> <span id="hp-play-text">Start Simulation</span>
                        </button>
                        <button onclick="resetHazardScenario()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold rounded-xl border border-slate-700">
                            🔄 Reset
                        </button>
                        <button onclick="toggleScoringWindowReveal()" id="hp-reveal-btn" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold rounded-xl border border-slate-700 flex items-center gap-1">
                            👁️ <span id="hp-reveal-text">Show 5-Pt Window</span>
                        </button>
                    </div>

                    <!-- Scrubber Slider -->
                    <div class="flex items-center gap-2 text-slate-400 font-mono flex-1 max-w-xs">
                        <span class="text-[11px]">Scrub:</span>
                        <input type="range" id="hp-scrubber" min="0" max="18" step="0.1" value="0" oninput="onScrubInput(this.value)" class="w-full accent-amber-500 cursor-pointer">
                    </div>

                    <!-- Live Score Outcome -->
                    <div id="hp-score-output" class="font-mono font-bold text-sm text-slate-400 px-3 py-1 bg-slate-950 rounded-lg border border-slate-800">
                        SCORE: <span class="text-white">--</span> / 5
                    </div>
                </div>
            </div>

            <!-- Post-Scenario Coaching Breakdown -->
            <div id="hp-coaching-box" class="bg-slate-900/90 p-5 rounded-xl border border-slate-800 space-y-4">
                <div class="flex items-center justify-between">
                    <h4 class="font-bold text-white text-sm flex items-center gap-2">
                        <span class="text-amber-400">Tactical Debrief:</span> Static Clue vs Developing Hazard
                    </h4>
                    <span id="hp-pulse-rating" class="text-xs px-2.5 py-1 rounded-full font-mono font-bold bg-slate-800 text-slate-400">Waiting for run...</span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80 space-y-1.5">
                        <span class="text-amber-400 font-bold block">1. The Static Clue (0 Points Zone)</span>
                        <p id="hp-desc-static" class="text-slate-400 leading-relaxed"></p>
                        <span class="text-[11px] text-rose-400 block font-semibold">⚠️ The Trap: Experienced drivers click too early here and lose points.</span>
                    </div>

                    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80 space-y-1.5">
                        <span class="text-emerald-400 font-bold block">2. The Developing Hazard (5 → 1 Points Zone)</span>
                        <p id="hp-desc-dev" class="text-slate-400 leading-relaxed"></p>
                        <span class="text-[11px] text-emerald-400 block font-semibold">✅ Highway Code Rule: <span id="hp-desc-rule" class="text-slate-300"></span></span>
                    </div>
                </div>

                <!-- 3-Click Pulse Assessment -->
                <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
                    <div class="space-y-0.5">
                        <span class="font-bold text-white">The Safe 3-Click Pulse Method Breakdown:</span>
                        <p class="text-slate-400 text-[11px]">Click 1 on initial clue, Click 2 (+0.8s) on movement commit, Click 3 (+1.0s) as camera slows.</p>
                    </div>
                    <div id="hp-pulse-telemetry" class="font-mono text-slate-300 bg-slate-900 px-3 py-1.5 rounded-lg border border-slate-800">
                        No clicks recorded yet
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

print("Module 2 generator ready.")
