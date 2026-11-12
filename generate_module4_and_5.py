def get_quiz_and_vault_html():
    return """
    <!-- MODULE 4: 85 HARDCORE TRAPS QUIZ & MOCK EXAM -->
    <div id="mod-quiz" class="space-y-6 hidden">
        <!-- Control Header & Mode Toggles -->
        <div class="bg-slate-900/90 rounded-2xl p-4 sm:p-6 border border-slate-800 space-y-4">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-amber-400">85 High-Fail Traps Quiz & Mock Exam Suite</span>
                        <span class="text-xs bg-amber-500/10 text-amber-400 border border-amber-500/30 px-2 py-0.5 rounded-full font-mono">100% High-Yield</span>
                    </h3>
                    <p class="text-xs text-slate-400">Filtered strictly for non-intuitive Highway Code rules, numeric limits, and trick questions.</p>
                </div>

                <!-- Study Mode Buttons -->
                <div class="flex items-center gap-1.5 bg-slate-950 p-1.5 rounded-xl border border-slate-800 flex-wrap">
                    <button onclick="setDrillMode('practice')" id="mode-btn-practice" class="px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 shadow">
                        🎯 Practice Drill
                    </button>
                    <button onclick="setDrillMode('mock')" id="mode-btn-mock" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white">
                        ⏱️ Timed Mock Exam (50 Qs)
                    </button>
                    <button onclick="setDrillMode('missed')" id="mode-btn-missed" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white flex items-center gap-1">
                        ❌ Missed Traps (<span id="missed-count-badge">0</span>)
                    </button>
                    <button onclick="setDrillMode('flashcard')" id="mode-btn-flashcard" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white">
                        🃏 3D Flashcards
                    </button>
                </div>
            </div>

            <!-- Category Filter Pills -->
            <div class="flex items-center gap-1.5 overflow-x-auto pb-1" id="quiz-category-pills">
                <!-- Dynamically populated category chips -->
            </div>

            <!-- Stats & Progress Bar -->
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 space-y-2">
                <div class="flex items-center justify-between text-xs font-mono">
                    <div class="flex items-center gap-3">
                        <span class="text-slate-400">CARD: <strong id="quiz-stat-card" class="text-white">1 / 85</strong></span>
                        <span class="text-slate-400">CORRECT: <strong id="quiz-stat-correct" class="text-emerald-400">0</strong></span>
                        <span class="text-slate-400">SCORE: <strong id="quiz-stat-acc" class="text-amber-400">0%</strong></span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span id="mock-timer-display" class="hidden text-rose-400 font-bold bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/30">⏳ 57:00</span>
                        <button onclick="resetQuizStats()" class="text-[11px] text-slate-500 hover:text-rose-400 transition underline">Reset History</button>
                    </div>
                </div>
                <div class="h-2 w-full bg-slate-900 rounded-full overflow-hidden">
                    <div id="quiz-progress-bar" class="h-full bg-amber-500 transition-all duration-300" style="width: 1%;"></div>
                </div>
            </div>
        </div>

        <!-- PRACTICE / QUIZ CARD VIEW -->
        <div id="quiz-card-container" class="max-w-3xl mx-auto">
            <!-- Dynamic Quiz Card -->
            <div class="bg-slate-900 rounded-2xl p-6 sm:p-8 border border-slate-800 shadow-xl space-y-6">
                <!-- Top Question Metadata -->
                <div class="flex items-center justify-between">
                    <span id="card-category-badge" class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-slate-800 text-amber-400 border border-slate-700">Studs & Motorways</span>
                    <span id="card-id-badge" class="text-xs font-mono text-slate-500">Q #1</span>
                </div>

                <!-- Sign Illustration (if present) -->
                <div id="card-sign-container" class="hidden flex justify-center py-2"></div>

                <!-- Question Text -->
                <h4 id="card-question-text" class="text-lg sm:text-xl font-bold text-white leading-relaxed">
                    Loading question...
                </h4>

                <!-- Multiple Choice Options -->
                <div id="card-options-grid" class="grid grid-cols-1 gap-3">
                    <!-- Options injected via JavaScript -->
                </div>

                <!-- Feedback & Explanation Box -->
                <div id="card-feedback-box" class="hidden p-4 rounded-xl border text-xs sm:text-sm space-y-2">
                    <div id="card-feedback-title" class="font-bold flex items-center gap-2 text-base"></div>
                    <p id="card-explanation-text" class="text-slate-300 leading-relaxed"></p>
                </div>

                <!-- Navigation Controls -->
                <div class="flex items-center justify-between pt-4 border-t border-slate-800 text-xs">
                    <button onclick="prevQuestion()" id="btn-prev-q" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold rounded-xl border border-slate-700">
                        ← Previous
                    </button>
                    <button onclick="nextQuestion()" id="btn-next-q" class="px-5 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold rounded-xl shadow transition">
                        Next Question →
                    </button>
                </div>
            </div>
        </div>

        <!-- 3D FLASHCARD VIEW (Hidden by default) -->
        <div id="flashcard-container" class="max-w-2xl mx-auto perspective-1000 hidden">
            <div id="flashcard-inner" onclick="flipFlashcard()" class="relative w-full h-[360px] transform-style-3d cursor-pointer select-none">
                <!-- Front Side -->
                <div class="absolute inset-0 backface-hidden bg-slate-900 rounded-2xl p-8 border border-slate-800 shadow-2xl flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span id="fc-category-front" class="text-xs font-mono font-bold text-amber-400">CATEGORY</span>
                        <span class="text-xs text-slate-500 font-mono">TAP TO FLIP 🔄</span>
                    </div>
                    <div class="text-center space-y-3">
                        <div id="fc-sign-front" class="hidden flex justify-center"></div>
                        <h4 id="fc-question-front" class="text-lg sm:text-xl font-bold text-white">Question prompt</h4>
                    </div>
                    <div class="text-center text-xs text-slate-500">
                        Click card or press <kbd class="px-1.5 py-0.5 bg-slate-800 text-slate-300 rounded font-mono">SPACE</kbd> to reveal answer
                    </div>
                </div>

                <!-- Back Side -->
                <div class="absolute inset-0 backface-hidden rotate-y-180 bg-slate-950 rounded-2xl p-8 border border-emerald-500/50 shadow-2xl flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-mono font-bold text-emerald-400">CORRECT ANSWER & RATIONALE</span>
                        <span class="text-xs text-slate-500 font-mono">TAP TO FLIP 🔄</span>
                    </div>
                    <div class="space-y-3">
                        <div id="fc-answer-back" class="text-lg sm:text-xl font-bold text-emerald-400">Answer</div>
                        <p id="fc-explanation-back" class="text-xs sm:text-sm text-slate-300 leading-relaxed"></p>
                    </div>
                    <div class="flex items-center justify-between pt-4 border-t border-slate-800 text-xs">
                        <button onclick="event.stopPropagation(); markFlashcard(false)" class="px-4 py-2 bg-rose-600/20 hover:bg-rose-600/40 text-rose-300 rounded-xl border border-rose-500/40">
                            Still Learning (Repeat)
                        </button>
                        <button onclick="event.stopPropagation(); markFlashcard(true)" class="px-4 py-2 bg-emerald-600/20 hover:bg-emerald-600/40 text-emerald-300 rounded-xl border border-emerald-500/40 font-bold">
                            Mastered ✓
                        </button>
                    </div>
                </div>
            </div>
            <div class="flex items-center justify-center gap-4 mt-4">
                <button onclick="prevQuestion()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-semibold">← Prev</button>
                <button onclick="nextQuestion()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-semibold">Next →</button>
            </div>
        </div>
    </div>

    <!-- MODULE 5: SEARCHABLE MASTER VAULT -->
    <div id="mod-vault" class="space-y-6 hidden">
        <div class="bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-4">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h3 class="text-xl font-bold text-white flex items-center gap-2">
                        <span class="text-emerald-400">Searchable Master Cheat Sheet Vault</span>
                        <span class="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded-full font-mono">Zero Fluff</span>
                    </h3>
                    <p class="text-xs text-slate-400">Type any keyword (e.g., "1.6mm", "scotland", "pelican", "snaking", "45 metres", "amber") to instantly filter all Highway Code numbers and rules.</p>
                </div>

                <!-- Search Input Bar -->
                <div class="relative w-full md:w-80">
                    <input type="text" id="vault-search-input" oninput="filterVaultTables(this.value)" placeholder="🔍 Search limits, rules, numbers..." class="w-full bg-slate-950 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 transition font-mono">
                    <button onclick="clearVaultSearch()" id="vault-clear-btn" class="absolute right-3 top-2.5 text-slate-500 hover:text-white text-xs hidden">✕</button>
                </div>
            </div>

            <!-- Live Count Indicator -->
            <div class="flex items-center justify-between text-xs text-slate-400 border-t border-slate-800 pt-3">
                <span>Showing filtered reference tables:</span>
                <button onclick="window.print()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold border border-slate-700 flex items-center gap-1">
                    🖨️ Print / Save Revision Summary
                </button>
            </div>
        </div>

        <!-- VAULT REFERENCE TABLES -->
        <div id="vault-tables-container" class="space-y-6">
            <!-- Table 1: Studs -->
            <div class="vault-card bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-3" data-keywords="cat eyes reflective studs red amber white green yellow contraflow motorway">
                <h4 class="font-bold text-white text-base flex items-center gap-2">
                    <span class="text-amber-400">1. Motorway & Dual Carriageway Reflective Studs (Cat's Eyes)</span>
                </h4>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left">
                        <thead>
                            <tr class="text-slate-400 border-b border-slate-800">
                                <th class="pb-2">Colour</th>
                                <th class="pb-2">Exact Placement on Carriageway</th>
                                <th class="pb-2">DVSA Exam Trigger Phrase</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 font-mono text-slate-300">
                            <tr>
                                <td class="py-2.5 font-bold text-rose-400">Red</td>
                                <td class="py-2.5">Left-hand edge of running carriageway</td>
                                <td class="py-2.5 font-sans">Separates normal lane from hard shoulder or verge</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-white">White</td>
                                <td class="py-2.5">Between running traffic lanes</td>
                                <td class="py-2.5 font-sans">Separates lanes travelling in the same direction</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-amber-400">Amber</td>
                                <td class="py-2.5">Right-hand edge of carriageway</td>
                                <td class="py-2.5 font-sans">Adjacent to central reservation / barrier</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-emerald-400">Green</td>
                                <td class="py-2.5">Slip road deceleration / acceleration lanes</td>
                                <td class="py-2.5 font-sans">Marks slip road entries and exits</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-lime-400">Fluorescent Green/Yellow</td>
                                <td class="py-2.5">Roadworks and contraflow systems</td>
                                <td class="py-2.5 font-sans">Temporary lane demarcations during construction</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Table 2: Stopping Distances -->
            <div class="vault-card bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-3" data-keywords="stopping thinking braking distance feet metres 20 30 40 50 60 70 car lengths dry wet ice">
                <h4 class="font-bold text-white text-base flex items-center gap-2">
                    <span class="text-sky-400">2. Dry Stopping Distances & Weather Multipliers</span>
                </h4>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left">
                        <thead>
                            <tr class="text-slate-400 border-b border-slate-800">
                                <th class="pb-2">Speed</th>
                                <th class="pb-2">Thinking Distance</th>
                                <th class="pb-2">Braking Multiplier</th>
                                <th class="pb-2">Braking Distance</th>
                                <th class="pb-2 text-amber-400 font-bold">Total Dry Distance</th>
                                <th class="pb-2">Car Lengths (4m)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 font-mono text-slate-300">
                            <tr>
                                <td class="py-2 font-bold text-white">20 mph</td>
                                <td class="py-2 text-sky-400">6 m (20 ft)</td>
                                <td class="py-2 text-slate-400">×1.0</td>
                                <td class="py-2 text-rose-400">6 m (20 ft)</td>
                                <td class="py-2 text-amber-400 font-bold">12 m (40 ft)</td>
                                <td class="py-2">3 cars</td>
                            </tr>
                            <tr>
                                <td class="py-2 font-bold text-white">30 mph</td>
                                <td class="py-2 text-sky-400">9 m (30 ft)</td>
                                <td class="py-2 text-slate-400">×1.5</td>
                                <td class="py-2 text-rose-400">14 m (45 ft)</td>
                                <td class="py-2 text-amber-400 font-bold">23 m (75 ft)</td>
                                <td class="py-2">6 cars</td>
                            </tr>
                            <tr>
                                <td class="py-2 font-bold text-white">40 mph</td>
                                <td class="py-2 text-sky-400">12 m (40 ft)</td>
                                <td class="py-2 text-slate-400">×2.0</td>
                                <td class="py-2 text-rose-400">24 m (80 ft)</td>
                                <td class="py-2 text-amber-400 font-bold">36 m (120 ft)</td>
                                <td class="py-2">9 cars</td>
                            </tr>
                            <tr>
                                <td class="py-2 font-bold text-white">50 mph</td>
                                <td class="py-2 text-sky-400">15 m (50 ft)</td>
                                <td class="py-2 text-slate-400">×2.5</td>
                                <td class="py-2 text-rose-400">38 m (125 ft)</td>
                                <td class="py-2 text-amber-400 font-bold">53 m (175 ft)</td>
                                <td class="py-2">13 cars</td>
                            </tr>
                            <tr>
                                <td class="py-2 font-bold text-white">60 mph</td>
                                <td class="py-2 text-sky-400">18 m (60 ft)</td>
                                <td class="py-2 text-slate-400">×3.0</td>
                                <td class="py-2 text-rose-400">55 m (180 ft)</td>
                                <td class="py-2 text-amber-400 font-bold">73 m (240 ft)</td>
                                <td class="py-2">18 cars</td>
                            </tr>
                            <tr>
                                <td class="py-2 font-bold text-white">70 mph</td>
                                <td class="py-2 text-sky-400">21 m (70 ft)</td>
                                <td class="py-2 text-slate-400">×3.5</td>
                                <td class="py-2 text-rose-400">75 m (245 ft)</td>
                                <td class="py-2 text-amber-400 font-bold">96 m (315 ft)</td>
                                <td class="py-2">24 cars</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs pt-2">
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                        <strong class="text-sky-400 block mb-1">🌧️ WET WEATHER RULE:</strong>
                        Multiply total dry stopping distance by <strong class="text-white">AT LEAST 2 (DOUBLE)</strong>. Gap: 4 seconds.
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800">
                        <strong class="text-indigo-400 block mb-1">❄️ ICY WEATHER RULE:</strong>
                        Multiply total dry stopping distance by <strong class="text-rose-400">UP TO 10 TIMES</strong>. Gap: 20 seconds.
                    </div>
                </div>
            </div>

            <!-- Table 3: Crossings -->
            <div class="vault-card bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-3" data-keywords="pedestrian crossings pelican puffin toucan pegasus zebra belisha flashing amber">
                <h4 class="font-bold text-white text-base flex items-center gap-2">
                    <span class="text-indigo-400">3. UK Pedestrian Crossings Comparison Matrix</span>
                </h4>
                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left">
                        <thead>
                            <tr class="text-slate-400 border-b border-slate-800">
                                <th class="pb-2">Crossing Type</th>
                                <th class="pb-2">Permitted Users</th>
                                <th class="pb-2">Flashing Amber?</th>
                                <th class="pb-2">Key Exam Feature</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 text-slate-300">
                            <tr>
                                <td class="py-2.5 font-bold text-amber-400">Pelican</td>
                                <td class="py-2.5">Pedestrians</td>
                                <td class="py-2.5 font-mono text-emerald-400 font-bold">YES</td>
                                <td class="py-2.5">Flashing amber = Give way to pedestrians on crossing; proceed if clear.</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-emerald-400">Puffin</td>
                                <td class="py-2.5">Pedestrians</td>
                                <td class="py-2.5 font-mono text-rose-400 font-bold">NO</td>
                                <td class="py-2.5">Infrared sensors detect pedestrians. Standard light cycle.</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-sky-400">Toucan</td>
                                <td class="py-2.5">Pedestrians & Cyclists</td>
                                <td class="py-2.5 font-mono text-rose-400 font-bold">NO</td>
                                <td class="py-2.5">"Two-can" cross together. Cyclists do NOT have to dismount.</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-purple-400">Pegasus</td>
                                <td class="py-2.5">Pedestrians & Horse Riders</td>
                                <td class="py-2.5 font-mono text-rose-400 font-bold">NO</td>
                                <td class="py-2.5">Push buttons mounted high on post for mounted equestrians.</td>
                            </tr>
                            <tr>
                                <td class="py-2.5 font-bold text-rose-400">Zebra</td>
                                <td class="py-2.5">Pedestrians</td>
                                <td class="py-2.5 font-mono text-amber-400">Belisha Beacons</td>
                                <td class="py-2.5">Must stop once pedestrian steps onto crossing. White zig-zags forbid parking/overtaking.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Table 4: Statutory Limits & Numbers -->
            <div class="vault-card bg-slate-900/90 rounded-2xl p-6 border border-slate-800 space-y-3" data-keywords="legal numbers thresholds tread 1.6mm alcohol breath blood urine scotland 35 22 mot 3 years sorn collision 24 hours 7 days hort1 horn 11:30 7:00">
                <h4 class="font-bold text-white text-base flex items-center gap-2">
                    <span class="text-rose-400">4. Statutory Limits, Alcohol & Documentation Thresholds</span>
                </h4>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">Tyre Tread Depth:</span>
                        <p class="text-slate-400"><strong class="text-amber-400">1.6 mm</strong> across the central three-quarters of the tread width and around the entire continuous circumference.</p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">Alcohol Limits:</span>
                        <p class="text-slate-400"><strong class="text-white">England/Wales:</strong> 35 mcg breath / 80 mg blood / 107 mg urine. <strong class="text-rose-400">Scotland:</strong> 22 mcg breath / 50 mg blood / 67 mg urine.</p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">Collision Reporting:</span>
                        <p class="text-slate-400">Within <strong class="text-amber-400">24 hours</strong> in person to police if insurance/contact details not exchanged at the scene.</p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">HO/RT1 Document Check:</span>
                        <p class="text-slate-400">Must produce licence, MOT, or insurance certificate within <strong class="text-amber-400">7 days</strong> at a nominated police station.</p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">New Drivers Act (Probation):</span>
                        <p class="text-slate-400"><strong class="text-rose-400">6 or more penalty points</strong> within 2 years of passing practical test = automatic revocation.</p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">First MOT & SORN:</span>
                        <p class="text-slate-400">First MOT at <strong class="text-amber-400">3 years old</strong>. SORN declaration remains valid <strong class="text-emerald-400">indefinitely</strong>.</p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">Horn Curfew:</span>
                        <p class="text-slate-400">Illegal between <strong class="text-amber-400">11:30 pm and 7:00 am</strong> in built-up areas, or when stationary.</p>
                    </div>
                    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 space-y-1">
                        <span class="font-bold text-white block">CPR Compressions:</span>
                        <p class="text-slate-400">Depth <strong class="text-amber-400">5 to 6 cm</strong> at rate of <strong class="text-emerald-400">100 to 120 per minute</strong>. Burns cooled for <strong class="text-sky-400">20 minutes</strong>.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

print("Module 4 and 5 generators ready.")
