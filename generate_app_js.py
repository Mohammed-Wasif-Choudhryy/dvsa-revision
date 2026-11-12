import json

def get_full_javascript():
    with open('all_questions.json', 'r', encoding='utf-8') as f:
        questions_json = json.dumps(json.load(f), indent=2)

    return f"""
    <script>
    // ==========================================
    // UK DVSA MASTER REVISION SYSTEM - JAVASCRIPT
    // ==========================================

    // 1. DATA: 85 CURATED TRAP QUESTIONS
    const QUESTIONS = {questions_json};

    // 2. DATA: 8 REALISTIC 3D COCKPIT HAZARD SCENARIOS
    const HP_SCENARIOS = [
        {{
            id: 0,
            name: "1. Zebra Crossing Distracted Pedestrian",
            env: "Urban High Street",
            speed: 30,
            duration: 18,
            winStart: 6.2,
            winEnd: 11.2,
            staticDesc: "0.0s – 6.2s: Pedestrian in yellow jacket walks parallel to road on left pavement looking at mobile phone. (Clicking here yields 0 points).",
            devDesc: "6.2s – 11.2s: Pedestrian suddenly pivots 90° towards road, steps onto Zebra stripes without looking, forcing you to brake.",
            hcode: "Rule 195: You MUST give way when a pedestrian has moved onto a crossing.",
            trap: "Clicking as soon as you see the pedestrian on the pavement. The DVSA codes this as a developing hazard only when they commit to stepping off the kerb.",
            type: "zebra"
        }},
        {{
            id: 1,
            name: "2. Blind Side Junction Delivery Van & Emerging Car",
            env: "Town Centre 30 mph",
            speed: 30,
            duration: 18,
            winStart: 5.8,
            winEnd: 10.8,
            staticDesc: "0.0s – 5.8s: Large delivery van parked on left kerb with amber hazards flashing, partially obscuring a side road T-junction.",
            devDesc: "5.8s – 10.8s: Silver car noses out past the double give-way lines from behind the van into your lane.",
            hcode: "Rule 170: Take extra care at junctions where view is restricted by parked vehicles.",
            trap: "Clicking immediately on the parked delivery van. A parked van with hazard lights is only a static hazard. The developing hazard begins when the silver car creeps past the Give Way line.",
            type: "junction"
        }},
        {{
            id: 2,
            name: "3. Country Lane Blind Bend & Horse with Rider",
            env: "Rural Single Carriageway",
            speed: 40,
            duration: 18,
            winStart: 6.5,
            winEnd: 11.5,
            staticDesc: "0.0s – 6.5s: Approaching a sharp right blind bend bordered by dense hedges on a narrow single carriageway.",
            devDesc: "6.5s – 11.5s: Horse and rider in hi-vis vest appear around the bend on the left, blocking half the carriageway.",
            hcode: "Rule 215: Pass horses wide and slow (max 10 mph). Give at least 2 metres of space and never sound your horn or rev your engine.",
            trap: "Clicking on the blind bend hedge itself before any actor appears. Window opens when the horse's head becomes visible.",
            type: "horse"
        }},
        {{
            id: 3,
            name: "4. Cyclist Swerving Around Deep Pothole",
            env: "Suburban Road 30 mph",
            speed: 30,
            duration: 18,
            winStart: 5.5,
            winEnd: 10.5,
            staticDesc: "0.0s – 5.5s: Cyclist riding normally along left gutter ahead of you.",
            devDesc: "5.5s – 10.5s: A large broken drain cover/pothole lies ahead; cyclist glances over right shoulder and swerves out into the centre of your lane.",
            hcode: "Rule 163 & 213: Leave at least 1.5 metres of room when overtaking cyclists at speeds up to 30 mph, and more space at higher speeds.",
            trap: "Clicking simply because a cyclist exists in front of you. The developing hazard only starts when the cyclist shoulder-checks and begins steering right.",
            type: "cyclist"
        }},
        {{
            id: 4,
            name: "5. Motorway Slip Road Reckless Cut-In",
            env: "3-Lane Motorway 70 mph",
            speed: 70,
            duration: 18,
            winStart: 6.0,
            winEnd: 11.0,
            staticDesc: "0.0s – 6.0s: Driving in Lane 1 of a 3-lane motorway. A slip road acceleration lane runs on your left with an HGV and a blue saloon behind it.",
            devDesc: "6.0s – 11.0s: The blue saloon aggressively accelerates, cuts across the painted solid white chevron markings, and forces its way directly into your lane.",
            hcode: "Rule 259: Joining traffic must give priority to traffic already on the motorway. Vehicles on the motorway should move to the middle lane if safe to do so.",
            trap: "Clicking on the slip road sign. The scoring window opens when the blue saloon begins encroaching across the solid white hatch markings.",
            type: "motorway"
        }},
        {{
            id: 5,
            name: "6. School Bus Blind Spot Child Running",
            env: "Residential 30 mph",
            speed: 30,
            duration: 18,
            winStart: 6.8,
            winEnd: 11.8,
            staticDesc: "0.0s – 6.8s: Yellow school bus pulled over at bus stop on left with hazard lights blinking.",
            devDesc: "6.8s – 11.8s: A child carrying a school bag sprints out from directly in front of the bus into your path to cross the road.",
            hcode: "Rule 209: Watch out for children emerging unexpectedly from behind or in front of stationary school buses or ice cream vans.",
            trap: "Clicking repeatedly on the stationary bus. The developing hazard is the child breaking into a run past the bus bumper.",
            type: "schoolbus"
        }},
        {{
            id: 6,
            name: "7. Emergency Ambulance at Signal Junction",
            env: "City Crossroad 30 mph",
            speed: 30,
            duration: 18,
            winStart: 5.2,
            winEnd: 10.2,
            staticDesc: "0.0s – 5.2s: Approaching green traffic lights at a 4-way crossroad junction.",
            devDesc: "5.2s – 10.2s: Emergency ambulance with flashing blue LED lights enters the crossroad from the right; lead car panic-brakes abruptly in your lane.",
            hcode: "Rule 219: Look and listen for ambulances, fire engines, police. Take appropriate action to let them pass without endangering other road users.",
            trap: "Clicking before you see or hear the emergency vehicle. Window opens when the blue strobes become visible and the lead car's brake lights illuminate.",
            type: "ambulance"
        }},
        {{
            id: 7,
            name: "8. Wet Weather Aquaplaning & Sudden Highway Braking",
            env: "Dual Carriageway (Torrential Rain)",
            speed: 60,
            duration: 18,
            winStart: 6.0,
            winEnd: 11.0,
            staticDesc: "0.0s – 6.0s: Driving on a dual carriageway in torrential rain with wipers clearing the windscreen. High spray.",
            devDesc: "6.0s – 11.0s: Lead vehicle hits a large pool of standing water in Lane 1, violently sprays water, and flashes red brake lights while beginning to slide.",
            hcode: "Rule 227: In wet weather, stopping distances are at least DOUBLE. Aquaplaning causes steering and braking to fail completely.",
            trap: "Clicking because it is raining. The developing hazard occurs when the lead car hits the standing pool and initiates emergency deceleration.",
            type: "rain"
        }}
    ];

    // 3. DATA: ACADEMY SIGNS & MARKS
    const ACADEMY_SIGNS = [
        {{
            title: "Clearway (No Stopping at any time)",
            type: "clearway",
            cat: "Prohibitory Orders",
            rule: "Rule 240",
            meaning: "Strictly NO STOPPING at ANY time on the main carriageway for any purpose, even momentarily to pick up or set down passengers.",
            trap: "Easily confused with No Waiting. A red cross X on a blue circle means NO STOPPING AT ALL."
        }},
        {{
            title: "No Waiting (Single Diagonal Bar)",
            type: "nowaiting",
            cat: "Prohibitory Orders",
            rule: "Rule 238",
            meaning: "Waiting prohibited during specified operational hours on time plate. You MAY stop briefly to drop off or pick up passengers.",
            trap: "Single red slash across blue circle = No Waiting. Full red X = Clearway."
        }},
        {{
            title: "Priority Over Oncoming Vehicles",
            type: "priority_you",
            cat: "Mandatory & Priority",
            rule: "Rule 155",
            meaning: "Blue rectangular sign. Large white up-arrow and small red down-arrow means YOU have priority over oncoming traffic.",
            trap: "White arrow = You go. Red arrow = You give way."
        }},
        {{
            title: "Give Priority to Oncoming Vehicles",
            type: "priority_oncoming",
            cat: "Prohibitory Orders",
            rule: "Rule 155",
            meaning: "White circle with red ring. Large red up-arrow and small black down-arrow means ONCOMING traffic has priority over you.",
            trap: "Circular sign with red border gives orders: you MUST give way."
        }},
        {{
            title: "Level Crossing WITH Gate or Barrier",
            type: "lc_gate",
            cat: "Warning Signs",
            rule: "Rule 291",
            meaning: "Triangular warning sign showing an old gate fence. Warns of railway level crossing fitted with barrier or gates.",
            trap: "Gate illustration = WITH barrier. Steam engine illustration = WITHOUT barrier."
        }},
        {{
            title: "Level Crossing WITHOUT Barrier",
            type: "lc_nogate",
            cat: "Warning Signs",
            rule: "Rule 291",
            meaning: "Triangular warning sign showing an old steam locomotive. Warns of open railway crossing WITHOUT gates or barriers.",
            trap: "Automatic open crossings often have twin alternating flashing red lights and alarm sirens."
        }},
        {{
            title: "Countdown Markers to Level Crossing",
            type: "countdown",
            cat: "Information & Distance",
            rule: "Rule 293",
            meaning: "White rectangular markers with slanted red bars: 3 bars = 300 yards (3/3), 2 bars = 200 yards (2/3), 1 bar = 100 yards (1/3).",
            trap: "Also used on motorway exit approaches (blue markers) and primary dual carriageways (green markers)."
        }},
        {{
            title: "Tram-Only Route",
            type: "tram_route",
            cat: "Mandatory Orders",
            rule: "Rule 300",
            meaning: "Blue circle with white tram symbol. Route reserved exclusively for trams. Other vehicles MUST NOT enter.",
            trap: "Trams cannot steer to avoid you and run silently. Always check rails when crossing."
        }},
        {{
            title: "Tram Stop / Proceed Signal",
            type: "tram_signal",
            cat: "Signals & Control",
            rule: "Rule 305",
            meaning: "White light signals on black background: Horizontal white bar = STOP. Vertical white bar = PROCEED.",
            trap: "These signals govern trams only, not road cars, but you must recognise them for the theory test."
        }},
        {{
            title: "No Vehicles (Prohibition of ALL Vehicles)",
            type: "no_vehicles",
            cat: "Prohibitory Orders",
            rule: "Rule 140",
            meaning: "Completely blank white circle with a red border. Strictly prohibits ALL vehicles, including bicycles.",
            trap: "A blank red ring is NOT derestriction. It means NO VEHICLES WHATSOEVER."
        }},
        {{
            title: "No Motor Vehicles",
            type: "no_motor_vehicles",
            cat: "Prohibitory Orders",
            rule: "Rule 140",
            meaning: "Red ring containing a car and a motorcycle. Prohibits all motor vehicles. Pedal cycles ARE permitted.",
            trap: "Distinguish from blank red circle: bicycles can enter here, but not in No Vehicles."
        }},
        {{
            title: "Mandatory Minimum Speed Limit (30 mph)",
            type: "min_speed",
            cat: "Mandatory Commands",
            rule: "Rule 124",
            meaning: "Solid blue circle with white number '30'. You MUST travel at or above 30 mph unless prevented by traffic.",
            trap: "Blue circles give positive mandatory orders. White circles with red rings give maximum speed limits."
        }},
        {{
            title: "End of Minimum Speed Limit",
            type: "end_min_speed",
            cat: "Mandatory Commands",
            rule: "Rule 124",
            meaning: "Solid blue circle with number '30' crossed by a diagonal red slash. Indicates the minimum speed limit has ended.",
            trap: "Frequently tested alongside tunnel exits."
        }},
        {{
            title: "National Speed Limit Applies",
            type: "national_speed_limit",
            cat: "Speed Signs",
            rule: "Rule 124",
            meaning: "White circle with black diagonal diagonal band. Means national speed limits apply: 60 single, 70 dual/motorway for cars.",
            trap: "Does NOT mean 70 everywhere! On a single carriageway it means 60 mph for cars, 50 mph for vans!"
        }},
        {{
            title: "Red Route: No Stopping at Any Time",
            type: "red_route",
            cat: "Kerb & Route Markings",
            rule: "Rule 240",
            meaning: "Double red lines along kerb. Strictly NO STOPPING at any time for any reason (even passenger drop-off).",
            trap: "Used heavily in London and West Midlands. Far stricter than double yellow lines."
        }},
        {{
            title: "Maximum Vehicle Height Limit",
            type: "low_bridge",
            cat: "Prohibitory Orders",
            rule: "Rule 137",
            meaning: "Red ring with inward vertical arrows. Indicates mandatory maximum vehicle height (e.g. 14′-6″ / 4.4m).",
            trap: "Inward arrows at top/bottom = HEIGHT. Inward arrows at left/right = WIDTH."
        }},
        {{
            title: "Zebra Crossing Ahead Warning",
            type: "zebra_sign",
            cat: "Warning Signs",
            rule: "Rule 195",
            meaning: "Blue rectangular or triangular sign with pedestrian on Zebra stripes. Prepare to stop for crossing pedestrians.",
            trap: "Accompanied on road by black-and-white road stripes and flashing yellow Belisha beacons."
        }},
        {{
            title: "School Crossing Patrol (Lollipop)",
            type: "school_crossing",
            cat: "Signals & Control",
            rule: "Rule 208",
            meaning: "Round yellow sign with 'STOP - CHILDREN'. You MUST stop when signalled by the patrol warden.",
            trap: "Offence to move until the patrol warden has fully returned to the pavement."
        }}
    ];

    // ==========================================
    // SVG RENDERING ENGINE FOR SIGNS
    // ==========================================
    function getSignSVG(type, sizeClass = "w-16 h-16") {{
        if (!type) return '';
        switch (type) {{
            case 'clearway':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#0284c7" stroke="#ef4444" stroke-width="10"/>
                    <line x1="20" y1="20" x2="80" y2="80" stroke="#ef4444" stroke-width="10"/>
                    <line x1="80" y1="20" x2="20" y2="80" stroke="#ef4444" stroke-width="10"/>
                </svg>`;
            case 'nowaiting':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#0284c7" stroke="#ef4444" stroke-width="10"/>
                    <line x1="20" y1="20" x2="80" y2="80" stroke="#ef4444" stroke-width="10"/>
                </svg>`;
            case 'priority_you':
                return `<svg class="${{sizeClass}} shadow-lg rounded-lg shrink-0" viewBox="0 0 100 100">
                    <rect x="6" y="6" width="88" height="88" rx="10" fill="#0284c7" stroke="#ffffff" stroke-width="4"/>
                    <path d="M35 80 L35 26 M22 40 L35 22 L48 40" stroke="#ffffff" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M68 22 L68 74 M58 62 L68 76 L78 62" stroke="#ef4444" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>`;
            case 'priority_oncoming':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#ffffff" stroke="#ef4444" stroke-width="10"/>
                    <path d="M36 74 L36 28 M27 38 L36 25 L45 38" stroke="#0f172a" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M64 26 L64 72 M52 58 L64 74 L76 58" stroke="#ef4444" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>`;
            case 'lc_gate':
                return `<svg class="${{sizeClass}} shadow-lg shrink-0" viewBox="0 0 100 100">
                    <path d="M50 10 L94 88 L6 88 Z" fill="#ffffff" stroke="#ef4444" stroke-width="9" stroke-linejoin="round"/>
                    <path d="M28 58 L72 58 M28 72 L72 72 M34 50 L34 78 M45 50 L45 78 M56 50 L56 78 M66 50 L66 78 M30 54 L70 76 M30 76 L70 54" stroke="#0f172a" stroke-width="3" fill="none"/>
                </svg>`;
            case 'lc_nogate':
                return `<svg class="${{sizeClass}} shadow-lg shrink-0" viewBox="0 0 100 100">
                    <path d="M50 10 L94 88 L6 88 Z" fill="#ffffff" stroke="#ef4444" stroke-width="9" stroke-linejoin="round"/>
                    <rect x="32" y="52" width="22" height="24" fill="#0f172a"/>
                    <rect x="54" y="60" width="18" height="16" fill="#0f172a"/>
                    <circle cx="38" cy="78" r="4" fill="#0f172a"/>
                    <circle cx="48" cy="78" r="4" fill="#0f172a"/>
                    <circle cx="62" cy="78" r="4" fill="#0f172a"/>
                    <rect x="62" y="52" width="6" height="8" fill="#0f172a"/>
                </svg>`;
            case 'countdown':
                return `<svg class="${{sizeClass}} shadow-lg rounded-lg shrink-0" viewBox="0 0 100 100">
                    <rect x="18" y="8" width="64" height="84" rx="4" fill="#ffffff" stroke="#0f172a" stroke-width="3"/>
                    <line x1="26" y1="36" x2="74" y2="20" stroke="#ef4444" stroke-width="9" stroke-linecap="round"/>
                    <line x1="26" y1="56" x2="74" y2="40" stroke="#ef4444" stroke-width="9" stroke-linecap="round"/>
                    <line x1="26" y1="76" x2="74" y2="60" stroke="#ef4444" stroke-width="9" stroke-linecap="round"/>
                </svg>`;
            case 'tram_route':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#0284c7" stroke="#ffffff" stroke-width="4"/>
                    <rect x="30" y="32" width="40" height="36" rx="4" fill="#ffffff"/>
                    <rect x="34" y="36" width="14" height="12" fill="#0284c7"/>
                    <rect x="52" y="36" width="14" height="12" fill="#0284c7"/>
                    <circle cx="38" cy="58" r="3" fill="#0284c7"/>
                    <circle cx="62" cy="58" r="3" fill="#0284c7"/>
                    <line x1="50" y1="32" x2="50" y2="22" stroke="#ffffff" stroke-width="3"/>
                    <line x1="42" y1="22" x2="58" y2="22" stroke="#ffffff" stroke-width="3"/>
                </svg>`;
            case 'tram_signal':
                return `<svg class="${{sizeClass}} shadow-lg rounded-xl shrink-0" viewBox="0 0 100 100">
                    <rect x="20" y="8" width="60" height="84" rx="6" fill="#0f172a" stroke="#475569" stroke-width="3"/>
                    <circle cx="50" cy="30" r="14" fill="#000000" stroke="#334155" stroke-width="2"/>
                    <circle cx="50" cy="68" r="14" fill="#000000" stroke="#334155" stroke-width="2"/>
                    <line x1="40" y1="30" x2="60" y2="30" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
                    <line x1="50" y1="58" x2="50" y2="78" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
                </svg>`;
            case 'no_vehicles':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#ffffff" stroke="#ef4444" stroke-width="12"/>
                </svg>`;
            case 'no_motor_vehicles':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#ffffff" stroke="#ef4444" stroke-width="10"/>
                    <rect x="30" y="32" width="40" height="20" rx="3" fill="#0f172a"/>
                    <circle cx="38" cy="52" r="4" fill="#0f172a"/>
                    <circle cx="62" cy="52" r="4" fill="#0f172a"/>
                    <circle cx="40" cy="72" r="4" fill="none" stroke="#0f172a" stroke-width="2"/>
                    <circle cx="60" cy="72" r="4" fill="none" stroke="#0f172a" stroke-width="2"/>
                    <path d="M40 72 L48 68 L54 68 L60 72" stroke="#0f172a" stroke-width="2" fill="none"/>
                </svg>`;
            case 'min_speed':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#0284c7" stroke="#ffffff" stroke-width="4"/>
                    <text x="50" y="62" text-anchor="middle" font-family="Inter, sans-serif" font-size="36" font-weight="800" fill="#ffffff">30</text>
                </svg>`;
            case 'end_min_speed':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#0284c7" stroke="#ffffff" stroke-width="4"/>
                    <text x="50" y="62" text-anchor="middle" font-family="Inter, sans-serif" font-size="36" font-weight="800" fill="#ffffff">30</text>
                    <line x1="20" y1="20" x2="80" y2="80" stroke="#ef4444" stroke-width="8"/>
                </svg>`;
            case 'national_speed_limit':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#ffffff" stroke="#0f172a" stroke-width="3"/>
                    <line x1="22" y1="78" x2="78" y2="22" stroke="#0f172a" stroke-width="12"/>
                </svg>`;
            case 'red_route':
                return `<svg class="${{sizeClass}} shadow-lg rounded-xl shrink-0" viewBox="0 0 100 100">
                    <rect x="8" y="14" width="84" height="72" rx="6" fill="#ffffff" stroke="#ef4444" stroke-width="4"/>
                    <line x1="20" y1="42" x2="80" y2="42" stroke="#ef4444" stroke-width="8"/>
                    <line x1="20" y1="58" x2="80" y2="58" stroke="#ef4444" stroke-width="8"/>
                    <text x="50" y="32" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="800" fill="#ef4444">RED ROUTE</text>
                </svg>`;
            case 'low_bridge':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#ffffff" stroke="#ef4444" stroke-width="10"/>
                    <polygon points="50,22 44,30 56,30" fill="#0f172a"/>
                    <polygon points="50,78 44,70 56,70" fill="#0f172a"/>
                    <text x="50" y="55" text-anchor="middle" font-family="Inter, sans-serif" font-size="16" font-weight="800" fill="#0f172a">14′-6″</text>
                </svg>`;
            case 'zebra_sign':
                return `<svg class="${{sizeClass}} shadow-lg rounded-lg shrink-0" viewBox="0 0 100 100">
                    <rect x="6" y="6" width="88" height="88" rx="8" fill="#0284c7" stroke="#ffffff" stroke-width="3"/>
                    <circle cx="50" cy="30" r="8" fill="#ffffff"/>
                    <path d="M42 42 L58 42 M50 42 L50 64 M50 64 L40 82 M50 64 L60 82" stroke="#ffffff" stroke-width="5" stroke-linecap="round"/>
                    <line x1="20" y1="84" x2="80" y2="84" stroke="#ffffff" stroke-width="4"/>
                </svg>`;
            case 'school_crossing':
                return `<svg class="${{sizeClass}} shadow-lg rounded-full shrink-0" viewBox="0 0 100 100">
                    <circle cx="50" cy="50" r="45" fill="#eab308" stroke="#0f172a" stroke-width="5"/>
                    <rect x="20" y="44" width="60" height="14" fill="#0f172a"/>
                    <text x="50" y="55" text-anchor="middle" font-family="Inter, sans-serif" font-size="12" font-weight="900" fill="#ffffff">STOP</text>
                    <text x="50" y="72" text-anchor="middle" font-family="Inter, sans-serif" font-size="9" font-weight="800" fill="#0f172a">CHILDREN</text>
                </svg>`;
            default:
                return '';
        }}
    }}

    function renderAcademySignCards() {{
        const grid = document.getElementById('academy-signs-grid');
        if (!grid) return;
        grid.innerHTML = ACADEMY_SIGNS.map(s => `
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 hover:border-slate-700 transition flex gap-4 items-start">
                ${{getSignSVG(s.type, "w-16 h-16")}}
                <div class="space-y-1 text-xs">
                    <div class="flex items-center justify-between">
                        <span class="text-amber-400 font-bold font-mono">${{s.cat}}</span>
                        <span class="text-[10px] text-slate-500 font-mono">${{s.rule}}</span>
                    </div>
                    <h5 class="font-bold text-white text-sm">${{s.title}}</h5>
                    <p class="text-slate-400 text-xs">${{s.meaning}}</p>
                    <div class="p-2 bg-slate-900 rounded-lg text-rose-300 text-[11px] font-medium border border-slate-800 mt-2">
                        ⚠️ <strong>Exam Trap:</strong> ${{s.trap}}
                    </div>
                </div>
            </div>
        `).join('');
    }}

    // ==========================================
    // TOP NAVIGATION & SUB-TAB SWITCHING
    // ==========================================
    function switchModule(modId) {{
        ['academy', 'hazard', 'labs', 'quiz', 'vault'].forEach(id => {{
            const el = document.getElementById('mod-' + id);
            const navBtn = document.getElementById('nav-' + id);
            if (el) el.classList.toggle('hidden', id !== modId);
            if (navBtn) {{
                if (id === modId) {{
                    navBtn.className = "px-3 py-2 rounded-lg transition-all whitespace-nowrap bg-amber-500 text-slate-950 font-bold shadow";
                }} else {{
                    navBtn.className = "px-3 py-2 rounded-lg transition-all whitespace-nowrap text-slate-400 hover:text-white hover:bg-slate-800/60 font-semibold";
                }}
            }}
        }});
        if (modId === 'hazard') {{
            initHazardCanvas();
        }}
    }}

    function switchAcademyTab(tabId) {{
        ['signs', 'mechanics', 'breakdowns', 'legal', 'speedlimits'].forEach(id => {{
            const el = document.getElementById('acad-sec-' + id);
            const btn = document.getElementById('acad-tab-' + id);
            if (el) el.classList.toggle('hidden', id !== tabId);
            if (btn) {{
                if (id === tabId) {{
                    btn.className = "acad-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-amber-500 text-slate-950 shadow";
                }} else {{
                    btn.className = "acad-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800";
                }}
            }}
        }});
    }}

    function switchLab(labId) {{
        ['stopping', 'studs', 'speedmatrix', 'crossings'].forEach(id => {{
            const el = document.getElementById('lab-sec-' + id);
            const btn = document.getElementById('lab-tab-' + id);
            if (el) el.classList.toggle('hidden', id !== labId);
            if (btn) {{
                if (id === labId) {{
                    btn.className = "lab-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-amber-500 text-slate-950 shadow";
                }} else {{
                    btn.className = "lab-tab-btn px-4 py-2 rounded-lg text-sm font-semibold bg-slate-900 text-slate-300 hover:bg-slate-800 border border-slate-800";
                }}
            }}
        }});
    }}

    // ==========================================
    // MODULE 2: 3D COCKPIT HAZARD PERCEPTION
    // ==========================================
    let hpCurrentIdx = 0;
    let hpTime = 0.0;
    let hpIsPlaying = false;
    let hpAnimId = null;
    let hpClicks = [];
    let hpAntiCheatTriggered = false;
    let hpScore = null;
    let hpRevealWindow = false;
    let hpMode = 'practice'; // 'practice' or 'exam'
    let hpSoundEnabled = true;

    // Web Audio Click Synthesizer
    let audioCtx = null;
    function playClickTone() {{
        if (!hpSoundEnabled) return;
        try {{
            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(800, audioCtx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(300, audioCtx.currentTime + 0.04);
            gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.04);
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.start();
            osc.stop(audioCtx.currentTime + 0.04);
        }} catch(e) {{}}
    }}

    function toggleHPSound() {{
        hpSoundEnabled = !hpSoundEnabled;
        const icon = document.getElementById('hp-sound-icon');
        const btn = document.getElementById('hp-sound-btn');
        if (icon) icon.textContent = hpSoundEnabled ? '🔊' : '🔇';
        if (btn) btn.innerHTML = `${{hpSoundEnabled ? '🔊' : '🔇'}} Sound: ${{hpSoundEnabled ? 'ON' : 'OFF'}}`;
    }}

    function setHPMode(mode) {{
        hpMode = mode;
        const btnPrac = document.getElementById('hp-mode-practice');
        const btnExam = document.getElementById('hp-mode-exam');
        const banner = document.getElementById('hp-live-coach-banner');
        if (mode === 'practice') {{
            btnPrac.className = "px-3 py-1.5 rounded-lg font-semibold bg-amber-500 text-slate-950 shadow";
            btnExam.className = "px-3 py-1.5 rounded-lg font-semibold text-slate-400 hover:text-white";
            if (banner) banner.classList.remove('hidden');
        }} else {{
            btnExam.className = "px-3 py-1.5 rounded-lg font-semibold bg-rose-500 text-white shadow";
            btnPrac.className = "px-3 py-1.5 rounded-lg font-semibold text-slate-400 hover:text-white";
            if (banner) banner.classList.add('hidden');
        }}
        resetHazardScenario();
    }}

    function renderHPButtons() {{
        const c = document.getElementById('hp-scenario-buttons');
        if (!c) return;
        c.innerHTML = HP_SCENARIOS.map((s, idx) => `
            <button onclick="selectHPScenario(${{idx}})" id="hp-sc-btn-${{idx}}" class="p-2 rounded-xl text-left border transition text-xs flex flex-col justify-between ${{idx === hpCurrentIdx ? 'bg-amber-500/10 border-amber-500 text-amber-400 font-bold' : 'bg-slate-950 border-slate-800 text-slate-400 hover:border-slate-700'}}">
                <span class="font-mono text-[10px] text-slate-500 block">SCENARIO ${{idx + 1}}</span>
                <span class="truncate font-semibold mt-1 block">${{s.name.split('. ')[1] || s.name}}</span>
            </button>
        `).join('');
    }}

    function selectHPScenario(idx) {{
        stopHazardScenario();
        hpCurrentIdx = idx;
        renderHPButtons();
        resetHazardScenario();
    }}

    function resetHazardScenario() {{
        stopHazardScenario();
        hpTime = 0.0;
        hpClicks = [];
        hpAntiCheatTriggered = false;
        hpScore = null;
        hpRevealWindow = (hpMode === 'practice');

        const s = HP_SCENARIOS[hpCurrentIdx];
        document.getElementById('hp-scenario-title').textContent = s.name;
        document.getElementById('hp-scenario-env').textContent = s.env;
        document.getElementById('hp-timer').textContent = "0.0s / " + s.duration.toFixed(1) + "s";
        document.getElementById('hp-click-count').textContent = "0";
        document.getElementById('hp-score-output').innerHTML = `SCORE: <span class="text-white">--</span> / 5`;
        document.getElementById('hp-anticheat-overlay').classList.add('hidden');
        document.getElementById('hp-scrubber').value = 0;
        document.getElementById('hp-scrubber').max = s.duration;

        document.getElementById('hp-desc-static').textContent = s.staticDesc;
        document.getElementById('hp-desc-dev').textContent = s.devDesc;
        document.getElementById('hp-desc-rule').textContent = s.hcode;
        document.getElementById('hp-pulse-rating').textContent = "Ready to start";
        document.getElementById('hp-pulse-rating').className = "text-xs px-2.5 py-1 rounded-full font-mono font-bold bg-slate-800 text-slate-400";
        document.getElementById('hp-pulse-telemetry').textContent = "Click or tap canvas to begin recording anticipation.";

        updateTimelineUI();
        draw3DCockpitCanvas();
    }}

    function toggleHazardPlay() {{
        if (hpIsPlaying) {{
            stopHazardScenario();
        }} else {{
            startHazardScenario();
        }}
    }}

    function startHazardScenario() {{
        if (hpAntiCheatTriggered) return;
        hpIsPlaying = true;
        document.getElementById('hp-play-icon').textContent = "⏸";
        document.getElementById('hp-play-text').textContent = "Pause Simulation";
        let lastTimestamp = performance.now();

        function loop(now) {{
            if (!hpIsPlaying) return;
            const dt = (now - lastTimestamp) / 1000;
            lastTimestamp = now;

            hpTime += dt;
            const s = HP_SCENARIOS[hpCurrentIdx];
            if (hpTime >= s.duration) {{
                hpTime = s.duration;
                stopHazardScenario();
                evaluateHPPerformance();
            }}

            updateHUD();
            updateTimelineUI();
            draw3DCockpitCanvas();
            hpAnimId = requestAnimationFrame(loop);
        }}
        hpAnimId = requestAnimationFrame(loop);
    }}

    function stopHazardScenario() {{
        hpIsPlaying = false;
        if (hpAnimId) cancelAnimationFrame(hpAnimId);
        document.getElementById('hp-play-icon').textContent = "▶";
        document.getElementById('hp-play-text').textContent = "Play Simulation";
    }}

    function onScrubInput(val) {{
        hpTime = parseFloat(val);
        updateHUD();
        updateTimelineUI();
        draw3DCockpitCanvas();
    }}

    function scrubTimeline(e) {{
        const track = document.getElementById('hp-timeline-track');
        const rect = track.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        const ratio = Math.max(0, Math.min(1, clickX / rect.width));
        const s = HP_SCENARIOS[hpCurrentIdx];
        hpTime = ratio * s.duration;
        document.getElementById('hp-scrubber').value = hpTime;
        updateHUD();
        updateTimelineUI();
        draw3DCockpitCanvas();
    }}

    function toggleScoringWindowReveal() {{
        hpRevealWindow = !hpRevealWindow;
        document.getElementById('hp-reveal-text').textContent = hpRevealWindow ? "Hide 5-Pt Window" : "Show 5-Pt Window";
        updateTimelineUI();
    }}

    function updateHUD() {{
        const s = HP_SCENARIOS[hpCurrentIdx];
        document.getElementById('hp-timer').textContent = hpTime.toFixed(1) + "s / " + s.duration.toFixed(1) + "s";
        document.getElementById('hp-scrubber').value = hpTime;

        // Practice Mode Live Hints
        const isWindowOpen = (hpTime >= s.winStart && hpTime <= s.winEnd);
        const bannerBadge = document.getElementById('hp-phase-badge');
        const bannerHint = document.getElementById('hp-phase-hint');
        const windowInd = document.getElementById('hp-window-indicator');
        const currentPts = document.getElementById('hp-current-pts');

        if (bannerBadge && bannerHint) {{
            if (hpTime < s.winStart) {{
                bannerBadge.textContent = "PHASE: STATIC CLUE (0 PTS)";
                bannerBadge.className = "px-2 py-0.5 rounded font-mono font-bold bg-slate-800 text-slate-400";
                bannerHint.textContent = "Potential hazard detected ahead. Do NOT click in single pulse yet.";
                if (windowInd) windowInd.classList.add('hidden');
            }} else if (hpTime <= s.winEnd) {{
                bannerBadge.textContent = "PHASE: DEVELOPING HAZARD!";
                bannerBadge.className = "px-2 py-0.5 rounded font-mono font-bold bg-emerald-500 text-slate-950";
                bannerHint.textContent = "Hazard is actively committing into your path! PULSE CLICK NOW!";
                if (windowInd) {{
                    windowInd.classList.remove('hidden');
                    const pts = computeClickScore(hpTime, s);
                    if (currentPts) currentPts.textContent = pts + " PTS";
                }}
            }} else {{
                bannerBadge.textContent = "PHASE: HAZARD RESOLVED";
                bannerBadge.className = "px-2 py-0.5 rounded font-mono font-bold bg-slate-800 text-slate-500";
                bannerHint.textContent = "Vehicle has slowed / hazard cleared.";
                if (windowInd) windowInd.classList.add('hidden');
            }}
        }}
    }}

    function recordHazardClick() {{
        if (!hpIsPlaying) {{
            startHazardScenario();
            return;
        }}
        if (hpAntiCheatTriggered) return;

        playClickTone();

        // Flash visual ripple
        const flash = document.getElementById('hp-click-flash');
        if (flash) {{
            flash.style.opacity = '1';
            setTimeout(() => {{ flash.style.opacity = '0'; }}, 100);
        }}

        const now = hpTime;
        hpClicks.push(now);
        document.getElementById('hp-click-count').textContent = hpClicks.length;

        // Anti-Cheat Algorithm Check:
        // 1. Spam filter: >3 clicks within 0.5s
        if (hpClicks.length >= 3) {{
            const last3 = hpClicks.slice(-3);
            if (last3[2] - last3[0] < 0.55) {{
                triggerAntiCheat("Rapid spam clicking detected (>3 clicks in 0.5s)");
                return;
            }}
        }}

        // 2. Metronome rhythmic clicking check: 4+ clicks with identical intervals (+-0.12s)
        if (hpClicks.length >= 4) {{
            const c = hpClicks.slice(-4);
            const d1 = c[1] - c[0];
            const d2 = c[2] - c[1];
            const d3 = c[3] - c[2];
            if (Math.abs(d1 - d2) < 0.12 && Math.abs(d2 - d3) < 0.12) {{
                triggerAntiCheat("Rhythmic metronome clicking detected (Anti-cheat rhythm pattern)");
                return;
            }}
        }}

        // 3. Excess clicks threshold
        if (hpClicks.length > 10) {{
            triggerAntiCheat("Exceeded maximum safe click threshold (10 clicks per clip)");
            return;
        }}

        updateTimelineUI();
    }}

    function triggerAntiCheat(reason) {{
        hpAntiCheatTriggered = true;
        stopHazardScenario();
        document.getElementById('hp-anticheat-reason').textContent = reason;
        document.getElementById('hp-anticheat-overlay').classList.remove('hidden');
        document.getElementById('hp-score-output').innerHTML = `SCORE: <span class="text-rose-500 font-black">0</span> / 5`;
    }}

    function computeClickScore(clickT, s) {{
        if (clickT < s.winStart || clickT > s.winEnd) return 0;
        const progress = (clickT - s.winStart) / (s.winEnd - s.winStart);
        if (progress <= 0.20) return 5;
        if (progress <= 0.40) return 4;
        if (progress <= 0.60) return 3;
        if (progress <= 0.80) return 2;
        return 1;
    }}

    function evaluateHPPerformance() {{
        const s = HP_SCENARIOS[hpCurrentIdx];
        if (hpAntiCheatTriggered) return;

        let maxScore = 0;
        hpClicks.forEach(c => {{
            const score = computeClickScore(c, s);
            if (score > maxScore) maxScore = score;
        }});
        hpScore = maxScore;

        const out = document.getElementById('hp-score-output');
        out.innerHTML = `SCORE: <span class="${{hpScore >= 4 ? 'text-emerald-400' : hpScore > 0 ? 'text-amber-400' : 'text-rose-400'}} font-bold text-lg">${{hpScore}}</span> / 5`;

        // Pulse telemetry evaluation
        const pulseRating = document.getElementById('hp-pulse-rating');
        const telemetry = document.getElementById('hp-pulse-telemetry');
        if (hpClicks.length === 0) {{
            pulseRating.textContent = "NO CLICKS RECORDED";
            pulseRating.className = "text-xs px-2.5 py-1 rounded-full font-mono font-bold bg-rose-500/20 text-rose-400 border border-rose-500/40";
            telemetry.textContent = "You missed the hazard completely. Watch for the commitment movement!";
        }} else if (hpScore === 5) {{
            pulseRating.textContent = "PERFECT 5/5 ANTICIPATION";
            pulseRating.className = "text-xs px-2.5 py-1 rounded-full font-mono font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/40";
            telemetry.textContent = `Caught the 5-point opening window cleanly at ${{hpClicks[0].toFixed(1)}}s. Flawless execution.`;
        }} else if (hpScore >= 3) {{
            pulseRating.textContent = `SOLID PASS (${{hpScore}}/5)`;
            pulseRating.className = "text-xs px-2.5 py-1 rounded-full font-mono font-bold bg-amber-500/20 text-amber-400 border border-amber-500/40";
            telemetry.textContent = `Captured ${{hpScore}} points. With a tighter 3-Click Pulse, Click 1 would have netted 5 points.`;
        }} else {{
            pulseRating.textContent = "0 POINTS: TIMING TRAP";
            pulseRating.className = "text-xs px-2.5 py-1 rounded-full font-mono font-bold bg-rose-500/20 text-rose-400 border border-rose-500/40";
            telemetry.textContent = `All clicks fell outside the 5-to-1 point window. Earliest click: ${{hpClicks[0].toFixed(1)}}s (Window opened at ${{s.winStart}}s).`;
        }}
    }}

    function updateTimelineUI() {{
        const s = HP_SCENARIOS[hpCurrentIdx];
        const playhead = document.getElementById('hp-playhead');
        const windowLayer = document.getElementById('hp-window-layer');
        const flagsLayer = document.getElementById('hp-flags-layer');

        // Playhead
        const pct = (hpTime / s.duration) * 100;
        if (playhead) playhead.style.left = pct + '%';

        // 5-Pt Window Highlight
        if (windowLayer) {{
            if (hpRevealWindow || hpMode === 'practice') {{
                const winLeft = (s.winStart / s.duration) * 100;
                const winWidth = ((s.winEnd - s.winStart) / s.duration) * 100;
                windowLayer.style.left = winLeft + '%';
                windowLayer.style.width = winWidth + '%';
                windowLayer.classList.remove('hidden');
            }} else {{
                windowLayer.classList.add('hidden');
            }}
        }}

        // Chevron Flags
        if (flagsLayer) {{
            flagsLayer.innerHTML = hpClicks.map((c, i) => {{
                const flagPct = (c / s.duration) * 100;
                return `<div class="absolute top-0 bottom-0 flex flex-col items-center pointer-events-none" style="left: ${{flagPct}}%;">
                    <div class="w-3 h-3 bg-rose-500 rotate-45 transform -translate-x-1.5 shadow-md border border-white"></div>
                    <span class="text-[9px] font-mono text-rose-300 font-bold bg-slate-950 px-0.5 rounded mt-0.5">${{i + 1}}</span>
                </div>`;
            }}).join('');
        }}
    }}

    // ==========================================
    // 3D COCKPIT PERSPECTIVE CANVAS ENGINE
    // ==========================================
    function initHazardCanvas() {{
        const canvas = document.getElementById('hp-canvas');
        if (!canvas) return;
        renderHPButtons();
        resetHazardScenario();
    }}

    // 3D Projection Helper
    function project3D(x, z, W, H, horizonY, curve = 0) {{
        if (z <= 0.8) z = 0.8;
        const camH = 1.25;
        const scale = (camH / z) * 280;
        const sx = (W * 0.5) + (x * scale) + (curve * (80 - z));
        const sy = horizonY + (camH / z) * 280;
        return {{ sx, sy, scale }};
    }}

    function draw3DCockpitCanvas() {{
        const canvas = document.getElementById('hp-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const W = canvas.width;
        const H = canvas.height;
        const s = HP_SCENARIOS[hpCurrentIdx];
        const t = hpTime;

        ctx.clearRect(0, 0, W, H);

        const horizonY = H * 0.44;
        const vpX = W * 0.5;

        // 1. SKY WITH ATMOSPHERIC GRADIENT
        const skyGrad = ctx.createLinearGradient(0, 0, 0, horizonY);
        if (s.type === 'rain') {{
            skyGrad.addColorStop(0, '#0f172a');
            skyGrad.addColorStop(0.6, '#1e293b');
            skyGrad.addColorStop(1, '#334155');
        }} else if (s.type === 'horse') {{
            skyGrad.addColorStop(0, '#0284c7');
            skyGrad.addColorStop(0.7, '#38bdf8');
            skyGrad.addColorStop(1, '#bae6fd');
        }} else {{
            skyGrad.addColorStop(0, '#1e293b');
            skyGrad.addColorStop(0.7, '#475569');
            skyGrad.addColorStop(1, '#94a3b8');
        }}
        ctx.fillStyle = skyGrad;
        ctx.fillRect(0, 0, W, horizonY);

        // Distant UK Rolling Hills
        ctx.fillStyle = s.type === 'rain' ? '#0f172a' : '#14532d';
        ctx.beginPath();
        ctx.moveTo(0, horizonY);
        ctx.bezierCurveTo(W * 0.25, horizonY - 18, W * 0.45, horizonY + 8, W * 0.65, horizonY - 12);
        ctx.bezierCurveTo(W * 0.8, horizonY - 24, W * 0.9, horizonY - 6, W, horizonY);
        ctx.lineTo(W, horizonY);
        ctx.lineTo(0, horizonY);
        ctx.fill();

        // 2. GROUND & PAVEMENTS / VERGES
        // Road verge base
        ctx.fillStyle = (s.type === 'horse' || s.type === 'motorway') ? '#15803d' : '#334155';
        ctx.fillRect(0, horizonY, W, H - horizonY);

        // Pavement left & right
        if (s.type !== 'motorway') {{
            ctx.fillStyle = '#64748b'; // stone pavement
            // Left sidewalk
            ctx.beginPath();
            ctx.moveTo(vpX - 42, horizonY);
            ctx.lineTo(0, H);
            ctx.lineTo(W * 0.16, H);
            ctx.lineTo(vpX - 25, horizonY);
            ctx.fill();

            // Right sidewalk
            ctx.beginPath();
            ctx.moveTo(vpX + 25, horizonY);
            ctx.lineTo(W * 0.84, H);
            ctx.lineTo(W, H);
            ctx.lineTo(vpX + 42, horizonY);
            ctx.fill();

            // Granite Kerbs
            ctx.fillStyle = '#94a3b8';
            ctx.beginPath();
            ctx.moveTo(vpX - 25, horizonY);
            ctx.lineTo(W * 0.16, H);
            ctx.lineTo(W * 0.18, H);
            ctx.lineTo(vpX - 22, horizonY);
            ctx.fill();

            ctx.beginPath();
            ctx.moveTo(vpX + 22, horizonY);
            ctx.lineTo(W * 0.82, H);
            ctx.lineTo(W * 0.84, H);
            ctx.lineTo(vpX + 25, horizonY);
            ctx.fill();
        }}

        // 3. ROAD SURFACE (Tarmac asphalt)
        ctx.fillStyle = s.type === 'rain' ? '#090d16' : '#1e293b';
        ctx.beginPath();
        ctx.moveTo(vpX - 22, horizonY);
        ctx.lineTo(W * 0.18, H);
        ctx.lineTo(W * 0.82, H);
        ctx.lineTo(vpX + 22, horizonY);
        ctx.fill();

        // Road Surface Reflection in Rain
        if (s.type === 'rain') {{
            ctx.fillStyle = 'rgba(255, 255, 255, 0.04)';
            ctx.beginPath();
            ctx.moveTo(vpX - 10, horizonY);
            ctx.lineTo(W * 0.42, H);
            ctx.lineTo(W * 0.58, H);
            ctx.lineTo(vpX + 10, horizonY);
            ctx.fill();
        }}

        // 4. ANIMATED ROAD MARKINGS (3D PERSPECTIVE)
        const roadSpeed = s.speed * 0.447; // mph to m/s
        const markLen = (s.type === 'motorway') ? 6.0 : 3.0;
        const gapLen = (s.type === 'motorway') ? 3.0 : 6.0;
        const cycle = markLen + gapLen;
        const offset = (t * roadSpeed) % cycle;

        ctx.fillStyle = '#f8fafc';
        // Center Dashed Dividing Line (Driving on LEFT!)
        for (let z = 60; z >= 2.5; z -= 0.6) {{
            const modDist = (z + offset) % cycle;
            if (modDist < markLen) {{
                const pNear = project3D(0, z, W, H, horizonY);
                const pFar = project3D(0, z + 0.6, W, H, horizonY);
                const wNear = Math.max(1, pNear.scale * 0.12);
                const wFar = Math.max(1, pFar.scale * 0.12);
                ctx.beginPath();
                ctx.moveTo(pFar.sx - wFar, pFar.sy);
                ctx.lineTo(pFar.sx + wFar, pFar.sy);
                ctx.lineTo(pNear.sx + wNear, pNear.sy);
                ctx.lineTo(pNear.sx - wNear, pNear.sy);
                ctx.fill();
            }}
        }}

        // 5. SCENARIO-SPECIFIC 3D ACTORS & HAZARDS
        const isDeveloping = (t >= s.winStart && t <= s.winEnd);

        if (s.type === 'zebra') {{
            // Zebra Crossing painted across road approaching ego car
            const zebraZ = Math.max(3.0, 48.0 - (t * 2.8));
            if (zebraZ > 2.0 && zebraZ < 55.0) {{
                ctx.fillStyle = '#ffffff';
                for (let x = -3.2; x <= 3.2; x += 0.8) {{
                    const z1 = project3D(x, zebraZ + 2.0, W, H, horizonY);
                    const z2 = project3D(x, zebraZ, W, H, horizonY);
                    ctx.fillRect(z1.sx - (z1.scale * 0.25), z1.sy, z1.scale * 0.5, z2.sy - z1.sy);
                }}

                // Belisha beacons flashing amber
                const flash = Math.floor(t * 3) % 2 === 0;
                const bLeft = project3D(-4.2, zebraZ, W, H, horizonY);
                const bRight = project3D(4.2, zebraZ, W, H, horizonY);
                ctx.fillStyle = flash ? '#f59e0b' : '#78350f';
                ctx.beginPath();
                ctx.arc(bLeft.sx, bLeft.sy - (bLeft.scale * 1.8), Math.max(3, bLeft.scale * 0.25), 0, Math.PI * 2);
                ctx.arc(bRight.sx, bRight.sy - (bRight.scale * 1.8), Math.max(3, bRight.scale * 0.25), 0, Math.PI * 2);
                ctx.fill();
            }}

            // Pedestrian on left pavement stepping out at 6.2s
            let pedX = -4.2;
            let pedZ = Math.max(3.0, 48.0 - (t * 2.8));
            let isCrossing = false;
            if (t > 6.2) {{
                isCrossing = true;
                pedX = -4.2 + (t - 6.2) * 1.1; // steps into left lane
            }}
            const pProj = project3D(pedX, pedZ, W, H, horizonY);
            draw3DPedestrian(ctx, pProj, t, isCrossing, isDeveloping);

        }} else if (s.type === 'junction') {{
            // Delivery Van parked on left side
            const vanZ = Math.max(4.0, 45.0 - (t * 2.6));
            const vanProj = project3D(-3.6, vanZ, W, H, horizonY);
            draw3DDeliveryVan(ctx, vanProj, true);

            // Silver car creeping past Give Way lines at 5.8s
            let carX = -5.8;
            let carZ = vanZ - 1.0;
            if (t > 5.8) {{
                carX = -5.8 + (t - 5.8) * 0.9; // encroaches into your running lane!
            }}
            const carProj = project3D(carX, carZ, W, H, horizonY);
            draw3DCar(ctx, carProj, true, false, '#94a3b8');

        }} else if (s.type === 'horse') {{
            // Sharp right blind bend hedge
            ctx.fillStyle = '#166534';
            for (let hz = 50; hz >= 5; hz -= 8) {{
                const hp = project3D(-4.5, hz, W, H, horizonY);
                ctx.beginPath();
                ctx.arc(hp.sx, hp.sy - (hp.scale * 1.5), hp.scale * 1.2, 0, Math.PI * 2);
                ctx.fill();
            }}
            // Horse & rider emerges around bend at 6.5s
            if (t > 3.0) {{
                const horseZ = Math.max(4.0, 52.0 - (t * 2.7));
                const horseX = (t > 6.5) ? -2.2 : -4.8;
                const horseProj = project3D(horseX, horseZ, W, H, horizonY);
                draw3DHorseAndRider(ctx, horseProj, t > 6.5, t);
            }}

        }} else if (s.type === 'cyclist') {{
            // Cyclist riding on left gutter
            let cycX = -3.2;
            let cycZ = Math.max(5.0, 50.0 - (t * 2.5));
            let isSwerving = false;
            // Pothole on road
            const potProj = project3D(-3.2, 24.0, W, H, horizonY);
            draw3DPothole(ctx, potProj);

            if (t > 5.5) {{
                isSwerving = true;
                cycX = -3.2 + (t - 5.5) * 0.7; // swerves right into lane center!
            }}
            const cycProj = project3D(cycX, cycZ, W, H, horizonY);
            draw3DCyclist(ctx, cycProj, isSwerving, t);

        }} else if (s.type === 'motorway') {{
            // 3-lane motorway with green reflective studs and merging traffic
            const hgvZ = Math.max(6.0, 60.0 - (t * 3.0));
            const hgvProj = project3D(-4.8, hgvZ, W, H, horizonY);
            draw3DDeliveryVan(ctx, hgvProj, false, '#475569');

            // Blue Saloon cutting in aggressively at 6.0s
            let saloonX = -5.5;
            let saloonZ = hgvZ + 4.0;
            if (t > 6.0) {{
                saloonX = -5.5 + (t - 6.0) * 1.4; // cuts across into Lane 1!
                saloonZ = Math.max(4.0, saloonZ - ((t - 6.0) * 1.2));
            }}
            const salProj = project3D(saloonX, saloonZ, W, H, horizonY);
            draw3DCar(ctx, salProj, false, true, '#2563eb');

        }} else if (s.type === 'schoolbus') {{
            // Yellow School Bus at bus stop
            const busZ = Math.max(5.0, 48.0 - (t * 2.6));
            const busProj = project3D(-3.8, busZ, W, H, horizonY);
            draw3DSchoolBus(ctx, busProj, true);

            // Child running out at 6.8s
            if (t > 6.8) {{
                const childX = -3.8 + (t - 6.8) * 1.5;
                const childZ = busZ - 1.5;
                const childProj = project3D(childX, childZ, W, H, horizonY);
                draw3DPedestrian(ctx, childProj, t, true, isDeveloping);
            }}

        }} else if (s.type === 'ambulance') {{
            // Emergency vehicle flashing blue strobes
            const ambZ = Math.max(4.0, 50.0 - (t * 3.0));
            const ambProj = project3D(2.4, ambZ, W, H, horizonY); // oncoming from right
            draw3DAmbulance(ctx, ambProj, true);

            // Lead car in your lane panic-brakes
            const leadCarZ = Math.max(4.0, 36.0 - (t * 2.2));
            const isPanicBrake = (t > 5.2);
            const leadProj = project3D(-1.8, leadCarZ, W, H, horizonY);
            draw3DCar(ctx, leadProj, isPanicBrake, false, '#10b981');

        }} else if (s.type === 'rain') {{
            // High spray & sudden lead car spin
            const leadZ = Math.max(4.0, 42.0 - (t * 2.4));
            const isSliding = (t > 6.0);
            const leadProj = project3D(-1.8 + (isSliding ? Math.sin(t * 12) * 0.4 : 0), leadZ, W, H, horizonY);
            draw3DCar(ctx, leadProj, isSliding, false, '#dc2626');

            // Rain drops on windscreen
            ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
            for (let i = 0; i < 40; i++) {{
                const rx = (i * 27 + t * 400) % W;
                const ry = (i * 39 + t * 600) % H;
                ctx.fillRect(rx, ry, 2, 8);
            }}
        }}

        // 6. COCKPIT INTERIOR & WINDSCREEN OVERLAY
        drawCockpitInterior(ctx, W, H, s, t);
    }}

    // ==========================================
    // 3D SPRITE DRAWING HELPERS
    // ==========================================
    function draw3DPedestrian(ctx, p, frame, isCrossing, isDanger) {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        const h = 1.7 * scale;
        const w = h * 0.4;
        const groundY = sy;
        const topY = sy - h;

        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.45)';
        ctx.beginPath();
        ctx.ellipse(sx, groundY, w * 0.6, w * 0.25, 0, 0, Math.PI * 2);
        ctx.fill();

        // Legs walking
        const stride = Math.sin(frame * 8) * (h * 0.15);
        ctx.strokeStyle = '#1e293b';
        ctx.lineWidth = Math.max(2, w * 0.22);
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(sx - w * 0.15, topY + h * 0.55);
        ctx.lineTo(sx - w * 0.15 + (isCrossing ? stride : 0), groundY);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(sx + w * 0.15, topY + h * 0.55);
        ctx.lineTo(sx + w * 0.15 - (isCrossing ? stride : 0), groundY);
        ctx.stroke();

        // Torso
        ctx.fillStyle = isDanger ? '#ef4444' : '#eab308';
        ctx.beginPath();
        ctx.roundRect(sx - w * 0.35, topY + h * 0.22, w * 0.7, h * 0.36, [Math.max(2, w * 0.1)]);
        ctx.fill();

        // Head
        ctx.fillStyle = '#fbcfe8';
        ctx.beginPath();
        ctx.arc(sx, topY + h * 0.12, Math.max(2, h * 0.09), 0, Math.PI * 2);
        ctx.fill();

        // Danger badge in practice mode
        if (isDanger && hpMode === 'practice') {{
            ctx.fillStyle = '#ef4444';
            ctx.font = `bold ${{Math.max(10, Math.round(scale * 0.35))}}px JetBrains Mono`;
            ctx.fillText('⚠️ HAZARD', sx - 25, topY - 8);
        }}
        ctx.restore();
    }}

    function draw3DCar(ctx, p, isBraking, isIndicatingRight, carColor = '#3b82f6') {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        const w = 1.8 * scale;
        const h = 1.4 * scale;
        const groundY = sy;
        const topY = sy - h;

        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.45)';
        ctx.beginPath();
        ctx.ellipse(sx, groundY, w * 0.55, h * 0.18, 0, 0, Math.PI * 2);
        ctx.fill();

        // Wheels
        ctx.fillStyle = '#0f172a';
        ctx.fillRect(sx - w * 0.48, groundY - h * 0.28, w * 0.18, h * 0.28);
        ctx.fillRect(sx + w * 0.30, groundY - h * 0.28, w * 0.18, h * 0.28);

        // Body
        ctx.fillStyle = carColor;
        ctx.beginPath();
        ctx.roundRect(sx - w * 0.45, topY + h * 0.35, w * 0.9, h * 0.48, [Math.max(3, w * 0.08)]);
        ctx.fill();

        // Roof / Cabin
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.moveTo(sx - w * 0.36, topY + h * 0.36);
        ctx.lineTo(sx - w * 0.28, topY);
        ctx.lineTo(sx + w * 0.28, topY);
        ctx.lineTo(sx + w * 0.36, topY + h * 0.36);
        ctx.closePath();
        ctx.fill();

        // Rear window
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.moveTo(sx - w * 0.33, topY + h * 0.34);
        ctx.lineTo(sx - w * 0.25, topY + h * 0.04);
        ctx.lineTo(sx + w * 0.25, topY + h * 0.04);
        ctx.lineTo(sx + w * 0.33, topY + h * 0.34);
        ctx.closePath();
        ctx.fill();

        // Yellow UK Number Plate
        ctx.fillStyle = '#facc15';
        ctx.fillRect(sx - w * 0.16, topY + h * 0.62, w * 0.32, h * 0.12);

        // Taillights & Brake Lights
        const tlW = w * 0.16;
        const tlH = h * 0.15;
        ctx.fillStyle = isBraking ? '#ff0000' : '#b91c1c';
        if (isBraking) {{
            ctx.shadowColor = '#ff0000';
            ctx.shadowBlur = Math.max(8, w * 0.25);
        }}
        ctx.fillRect(sx - w * 0.43, topY + h * 0.42, tlW, tlH);
        ctx.fillRect(sx + w * 0.27, topY + h * 0.42, tlW, tlH);
        ctx.shadowBlur = 0;

        // Turn indicator
        if (isIndicatingRight && (Math.floor(Date.now() / 320) % 2 === 0)) {{
            ctx.fillStyle = '#f59e0b';
            ctx.shadowColor = '#f59e0b';
            ctx.shadowBlur = 12;
            ctx.fillRect(sx + w * 0.32, topY + h * 0.42, tlW * 0.7, tlH);
            ctx.shadowBlur = 0;
        }}
        ctx.restore();
    }}

    function draw3DDeliveryVan(ctx, p, isHazardFlashing, vanColor = '#4338ca') {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        const w = 2.1 * scale;
        const h = 2.0 * scale;
        const groundY = sy;
        const topY = sy - h;

        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
        ctx.beginPath();
        ctx.ellipse(sx, groundY, w * 0.55, h * 0.15, 0, 0, Math.PI * 2);
        ctx.fill();

        // Box body
        ctx.fillStyle = vanColor;
        ctx.beginPath();
        ctx.roundRect(sx - w * 0.48, topY, w * 0.96, h * 0.85, [Math.max(3, w * 0.05)]);
        ctx.fill();

        // Rear Doors seam
        ctx.strokeStyle = '#1e1b4b';
        ctx.lineWidth = Math.max(1, w * 0.02);
        ctx.beginPath();
        ctx.moveTo(sx, topY + h * 0.1);
        ctx.lineTo(sx, groundY - h * 0.18);
        ctx.stroke();

        // Hazard lights flashing
        if (isHazardFlashing && (Math.floor(Date.now() / 350) % 2 === 0)) {{
            ctx.fillStyle = '#f59e0b';
            ctx.shadowColor = '#f59e0b';
            ctx.shadowBlur = 14;
            ctx.fillRect(sx - w * 0.46, topY + h * 0.6, w * 0.15, h * 0.1);
            ctx.fillRect(sx + w * 0.31, topY + h * 0.6, w * 0.15, h * 0.1);
            ctx.shadowBlur = 0;
        }}
        ctx.restore();
    }}

    function draw3DCyclist(ctx, p, isSwerving, frame) {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        const h = 1.7 * scale;
        const w = 0.8 * scale;
        const groundY = sy;
        const topY = sy - h;

        ctx.save();
        // Bicycle wheels
        ctx.strokeStyle = '#0f172a';
        ctx.lineWidth = Math.max(2, w * 0.08);
        ctx.beginPath();
        ctx.arc(sx - w * 0.35, groundY - h * 0.15, h * 0.15, 0, Math.PI * 2);
        ctx.arc(sx + w * 0.35, groundY - h * 0.15, h * 0.15, 0, Math.PI * 2);
        ctx.stroke();

        // Bicycle Frame
        ctx.strokeStyle = '#38bdf8';
        ctx.beginPath();
        ctx.moveTo(sx - w * 0.35, groundY - h * 0.15);
        ctx.lineTo(sx, groundY - h * 0.35);
        ctx.lineTo(sx + w * 0.35, groundY - h * 0.15);
        ctx.stroke();

        // Rider (Hi-vis vest)
        ctx.fillStyle = '#eab308';
        ctx.beginPath();
        ctx.roundRect(sx - w * 0.22, topY + h * 0.28, w * 0.44, h * 0.38, [3]);
        ctx.fill();

        // Helmet
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.arc(sx, topY + h * 0.18, h * 0.12, 0, Math.PI * 2);
        ctx.fill();

        // Right Arm sticking out to signal right if swerving
        if (isSwerving) {{
            ctx.strokeStyle = '#eab308';
            ctx.lineWidth = Math.max(3, w * 0.12);
            ctx.beginPath();
            ctx.moveTo(sx + w * 0.2, topY + h * 0.35);
            ctx.lineTo(sx + w * 0.8, topY + h * 0.35);
            ctx.stroke();
        }}
        ctx.restore();
    }}

    function draw3DHorseAndRider(ctx, p, isApproaching, frame) {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        const h = 2.2 * scale;
        const w = 1.6 * scale;
        const groundY = sy;
        const topY = sy - h;

        ctx.save();
        // Horse body
        ctx.fillStyle = '#78350f'; // rich brown
        ctx.beginPath();
        ctx.ellipse(sx, groundY - h * 0.35, w * 0.45, h * 0.22, 0, 0, Math.PI * 2);
        ctx.fill();

        // Horse Head & Neck
        ctx.beginPath();
        ctx.moveTo(sx + w * 0.3, groundY - h * 0.4);
        ctx.lineTo(sx + w * 0.45, groundY - h * 0.65);
        ctx.lineTo(sx + w * 0.25, groundY - h * 0.65);
        ctx.closePath();
        ctx.fill();

        // Horse legs
        ctx.strokeStyle = '#451a03';
        ctx.lineWidth = Math.max(2, w * 0.08);
        ctx.beginPath();
        ctx.moveTo(sx - w * 0.3, groundY - h * 0.3);
        ctx.lineTo(sx - w * 0.3, groundY);
        ctx.moveTo(sx + w * 0.3, groundY - h * 0.3);
        ctx.lineTo(sx + w * 0.3, groundY);
        ctx.stroke();

        // Rider (Fluorescent Pink / Yellow Tabard)
        ctx.fillStyle = '#ec4899';
        ctx.beginPath();
        ctx.roundRect(sx - w * 0.18, topY + h * 0.2, w * 0.36, h * 0.3, [3]);
        ctx.fill();

        // Riding Hat
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.arc(sx, topY + h * 0.15, h * 0.1, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
    }}

    function draw3DSchoolBus(ctx, p, isHazardFlashing) {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        const w = 2.4 * scale;
        const h = 2.6 * scale;
        const groundY = sy;
        const topY = sy - h;

        ctx.save();
        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
        ctx.beginPath();
        ctx.ellipse(sx, groundY, w * 0.55, h * 0.12, 0, 0, Math.PI * 2);
        ctx.fill();

        // Yellow Bus Body
        ctx.fillStyle = '#eab308';
        ctx.beginPath();
        ctx.roundRect(sx - w * 0.48, topY, w * 0.96, h * 0.85, [Math.max(4, w * 0.06)]);
        ctx.fill();

        // Rear Windows
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(sx - w * 0.4, topY + h * 0.15, w * 0.8, h * 0.25);

        // School Children warning sign
        ctx.fillStyle = '#facc15';
        ctx.fillRect(sx - w * 0.2, topY + h * 0.5, w * 0.4, h * 0.18);
        ctx.fillStyle = '#000000';
        ctx.font = `bold ${{Math.max(7, Math.round(w * 0.08))}}px sans-serif`;
        ctx.textAlign = 'center';
        ctx.fillText('SCHOOL BUS', sx, topY + h * 0.62);

        // Hazards
        if (isHazardFlashing && (Math.floor(Date.now() / 320) % 2 === 0)) {{
            ctx.fillStyle = '#f59e0b';
            ctx.shadowColor = '#f59e0b';
            ctx.shadowBlur = 12;
            ctx.fillRect(sx - w * 0.44, topY + h * 0.7, w * 0.14, h * 0.1);
            ctx.fillRect(sx + w * 0.30, topY + h * 0.7, w * 0.14, h * 0.1);
            ctx.shadowBlur = 0;
        }}
        ctx.restore();
    }}

    function draw3DAmbulance(ctx, p, isStrobeFlashing) {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        const w = 2.2 * scale;
        const h = 2.2 * scale;
        const groundY = sy;
        const topY = sy - h;

        ctx.save();
        // White Body
        ctx.fillStyle = '#ffffff';
        ctx.beginPath();
        ctx.roundRect(sx - w * 0.46, topY + h * 0.1, w * 0.92, h * 0.78, [4]);
        ctx.fill();

        // Battenburg green/yellow checks
        ctx.fillStyle = '#15803d';
        ctx.fillRect(sx - w * 0.46, topY + h * 0.45, w * 0.46, h * 0.15);
        ctx.fillStyle = '#facc15';
        ctx.fillRect(sx, topY + h * 0.45, w * 0.46, h * 0.15);

        // Roof Blue Strobes
        if (isStrobeFlashing) {{
            const flash = (Math.floor(Date.now() / 150) % 2 === 0);
            ctx.fillStyle = flash ? '#38bdf8' : '#1d4ed8';
            ctx.shadowColor = '#38bdf8';
            ctx.shadowBlur = 18;
            ctx.fillRect(sx - w * 0.35, topY, w * 0.7, h * 0.1);
            ctx.shadowBlur = 0;
        }}
        ctx.restore();
    }}

    function draw3DPothole(ctx, p) {{
        const {{ sx, sy, scale }} = p;
        if (scale <= 0) return;
        ctx.save();
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.ellipse(sx, sy, scale * 0.5, scale * 0.2, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = '#475569';
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.restore();
    }}

    // 7. COCKPIT INTERIOR FOREGROUND (Windscreen, Dashboard & Right-Hand Wheel)
    function drawCockpitInterior(ctx, W, H, s, t) {{
        ctx.save();

        // Windscreen A-Pillars
        ctx.fillStyle = '#020617';
        // Left pillar
        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(W * 0.06, 0);
        ctx.lineTo(W * 0.15, H);
        ctx.lineTo(0, H);
        ctx.fill();
        // Right pillar
        ctx.beginPath();
        ctx.moveTo(W, 0);
        ctx.lineTo(W * 0.94, 0);
        ctx.lineTo(W * 0.85, H);
        ctx.lineTo(W, H);
        ctx.fill();

        // Car Bonnet Curve (bottom center)
        ctx.fillStyle = '#090d16';
        ctx.beginPath();
        ctx.moveTo(W * 0.20, H);
        ctx.bezierCurveTo(W * 0.34, H * 0.80, W * 0.66, H * 0.80, W * 0.80, H);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Dashboard Console Band across bottom
        ctx.fillStyle = '#020617';
        ctx.fillRect(0, H - 54, W, 54);
        ctx.strokeStyle = '#1e293b';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, H - 54);
        ctx.lineTo(W, H - 54);
        ctx.stroke();

        // STEERING WHEEL ON RIGHT (UK DRIVER SEAT!)
        const wheelX = W * 0.74;
        const wheelY = H - 15;
        ctx.beginPath();
        ctx.arc(wheelX, wheelY, 95, 0, Math.PI * 2);
        ctx.strokeStyle = '#1e293b';
        ctx.lineWidth = 16;
        ctx.stroke();
        // Spokes
        ctx.lineWidth = 10;
        ctx.beginPath();
        ctx.moveTo(wheelX - 90, wheelY);
        ctx.lineTo(wheelX + 90, wheelY);
        ctx.moveTo(wheelX, wheelY);
        ctx.lineTo(wheelX, wheelY + 80);
        ctx.stroke();
        // Center boss
        ctx.beginPath();
        ctx.arc(wheelX, wheelY, 28, 0, Math.PI * 2);
        ctx.fillStyle = '#0f172a';
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2;
        ctx.stroke();

        // REARVIEW MIRROR (Top Center)
        ctx.fillStyle = '#1e293b';
        ctx.beginPath();
        ctx.roundRect(W * 0.38, 12, W * 0.24, 48, [10]);
        ctx.fill();
        ctx.strokeStyle = '#64748b';
        ctx.lineWidth = 2;
        ctx.stroke();
        // Mirror Glass
        ctx.fillStyle = '#090d16';
        ctx.beginPath();
        ctx.roundRect(W * 0.38 + 3, 15, W * 0.24 - 6, 42, [8]);
        ctx.fill();
        // Road reflection in mirror
        ctx.fillStyle = '#334155';
        ctx.beginPath();
        ctx.moveTo(W * 0.50, 18);
        ctx.lineTo(W * 0.42, 54);
        ctx.lineTo(W * 0.58, 54);
        ctx.fill();
        ctx.fillStyle = '#94a3b8';
        ctx.font = 'bold 9px JetBrains Mono';
        ctx.fillText('REARVIEW MIRROR', W * 0.43, 28);

        // DASHBOARD HUD INSTRUMENT CLUSTER
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.roundRect(W * 0.24, H - 50, 150, 44, [8]);
        ctx.fill();
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Speedometer text
        ctx.fillStyle = '#94a3b8';
        ctx.font = 'bold 9px JetBrains Mono';
        ctx.fillText('SPEED (UK)', W * 0.25, H - 36);
        ctx.fillStyle = '#38bdf8';
        ctx.font = 'bold 18px JetBrains Mono';
        ctx.fillText(`${{s.speed}} MPH`, W * 0.25, H - 16);

        // Rain Windscreen Wipers Animation
        if (s.type === 'rain') {{
            const wiperAngle = Math.sin(t * 5) * 0.7;
            ctx.strokeStyle = '#020617';
            ctx.lineWidth = 6;
            ctx.lineCap = 'round';
            // Driver wiper
            ctx.beginPath();
            ctx.moveTo(W * 0.65, H - 54);
            ctx.lineTo(W * 0.65 + Math.cos(-Math.PI / 2 + wiperAngle) * 160, (H - 54) + Math.sin(-Math.PI / 2 + wiperAngle) * 160);
            ctx.stroke();
            // Passenger wiper
            ctx.beginPath();
            ctx.moveTo(W * 0.35, H - 54);
            ctx.lineTo(W * 0.35 + Math.cos(-Math.PI / 2 + wiperAngle) * 160, (H - 54) + Math.sin(-Math.PI / 2 + wiperAngle) * 160);
            ctx.stroke();
        }}

        ctx.restore();
    }}

    // ==========================================
    // MODULE 3: INTERACTIVE LABS LOGIC
    // ==========================================
    let labStoppingSpeed = 30;
    let labWeather = 'dry';

    function setStoppingSpeed(mph) {{
        labStoppingSpeed = mph;
        [20, 30, 40, 50, 60, 70].forEach(s => {{
            const btn = document.getElementById('speed-btn-' + s);
            if (btn) {{
                if (s === mph) {{
                    btn.className = "speed-selector-btn py-3 px-2 rounded-xl text-center bg-amber-500 text-slate-950 font-mono font-bold text-sm shadow";
                }} else {{
                    btn.className = "speed-selector-btn py-3 px-2 rounded-xl text-center bg-slate-950 hover:bg-slate-800 border border-slate-800 font-mono font-bold text-sm";
                }}
            }}
        }});
        updateStoppingUI();
    }}

    function setWeather(cond) {{
        labWeather = cond;
        ['dry', 'wet', 'ice'].forEach(c => {{
            const btn = document.getElementById('weather-' + c);
            if (btn) {{
                if (c === cond) {{
                    btn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 shadow";
                }} else {{
                    btn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white";
                }}
            }}
        }});
        updateStoppingUI();
    }}

    function updateStoppingUI() {{
        const mph = labStoppingSpeed;
        const thinkingFt = mph; // ALWAYS equals speed in feet!
        const thinkingM = Math.round(thinkingFt * 0.3048);

        // Braking multipliers: 20x1.0, 30x1.5, 40x2.0, 50x2.5, 60x3.0, 70x3.5
        const mult = 1.0 + ((mph - 20) / 10) * 0.5;
        let brakingFt = Math.round(mph * mult);
        let weatherMult = 1;
        if (labWeather === 'wet') weatherMult = 2;
        if (labWeather === 'ice') weatherMult = 10;

        brakingFt *= weatherMult;
        const brakingM = Math.round(brakingFt * 0.3048);

        const totalFt = thinkingFt + brakingFt;
        const totalM = thinkingM + brakingM;
        const carLengths = Math.round(totalM / 4.0);

        document.getElementById('out-thinking-m').textContent = `${{thinkingM}} metres`;
        document.getElementById('out-thinking-ft').textContent = `${{thinkingFt}} feet`;
        document.getElementById('out-braking-m').textContent = `${{brakingM}} metres`;
        document.getElementById('out-braking-ft').textContent = `${{brakingFt}} feet`;
        document.getElementById('out-braking-formula').textContent = `Formula: ${{mph}} × ${{mult.toFixed(1)}}${{weatherMult > 1 ? ' × ' + weatherMult : ''}} = ${{brakingFt}} ft`;

        document.getElementById('out-total-m').textContent = `${{totalM}} metres`;
        document.getElementById('out-total-ft').innerHTML = `${{totalFt}} feet (<span id="out-car-lengths">${{carLengths}}</span> car lengths)`;

        const note = document.getElementById('out-weather-note');
        if (labWeather === 'dry') note.textContent = "Dry road baseline (1 car = 4 metres)";
        else if (labWeather === 'wet') note.textContent = "🌧️ WET: Braking distance doubled (x2 multiplier)";
        else note.textContent = "❄️ ICE: Braking distance increased by up to 10 times (x10)";

        // Visual Proportion Bar
        const tRatio = Math.round((thinkingFt / totalFt) * 100);
        const bRatio = 100 - tRatio;
        document.getElementById('bar-thinking').style.width = tRatio + '%';
        document.getElementById('bar-braking').style.width = bRatio + '%';
        document.getElementById('out-bar-ratio').textContent = `Thinking: ${{tRatio}}% | Braking: ${{bRatio}}%`;
    }}

    // Motorway Studs Interactive
    const STUDS_DATA = {{
        red: {{
            title: "RED STUDS — Left Hard Shoulder & Boundary",
            desc: "Red studs mark the left-hand edge of the running carriageway next to the hard shoulder or verge. They prevent drivers drifting off the motorway into the ditch."
        }},
        white: {{
            title: "WHITE STUDS — Lane Demarcation",
            desc: "White studs separate normal traffic lanes travelling in the same direction. Keep between them unless safely overtaking."
        }},
        amber: {{
            title: "AMBER STUDS — Central Reservation",
            desc: "Amber studs mark the far-right edge of the carriageway adjacent to the central reservation barrier."
        }},
        green: {{
            title: "GREEN STUDS — Slip Road Entries & Exits",
            desc: "Green studs mark deceleration and acceleration lanes where slip roads join or leave the main motorway carriageway."
        }},
        yellow: {{
            title: "FLUORESCENT GREEN / YELLOW STUDS — Roadworks & Contraflow",
            desc: "Bright fluorescent green/yellow studs indicate temporary lane layouts and contraflow diversions through active highway roadworks."
        }}
    }};

    function selectStud(colour) {{
        const info = STUDS_DATA[colour];
        if (!info) return;
        document.getElementById('stud-detail-title').textContent = info.title;
        document.getElementById('stud-detail-desc').textContent = info.desc;
    }}

    let isContraflow = false;
    function toggleContraflow() {{
        isContraflow = !isContraflow;
        document.getElementById('btn-contraflow').className = isContraflow ?
            "px-3 py-1.5 rounded-lg text-xs font-semibold bg-lime-500 text-slate-950 shadow" :
            "px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700";
        selectStud(isContraflow ? 'yellow' : 'white');
    }}

    function toggleGantryLane(laneNum) {{
        const valEl = document.getElementById('gantry-val-' + laneNum);
        if (!valEl) return;
        if (valEl.textContent === '✕') {{
            valEl.textContent = '60';
            valEl.className = 'text-2xl font-bold text-emerald-400 mb-1';
        }} else {{
            valEl.textContent = '✕';
            valEl.className = 'text-2xl font-bold text-red-500 font-black mb-1 animate-pulse';
        }}
    }}

    // Vehicle Speed Limit Selector
    const VEHICLE_LIMITS = {{
        car: {{ builtup: 30, single: 60, dual: 70, motorway: 70, note: "Cars, motorbikes, and car-derived vans (<2t) have the highest national limits." }},
        car_derived: {{ builtup: 30, single: 60, dual: 70, motorway: 70, note: "Car-derived vans under 2 tonnes max laden weight are legally classified with cars!" }},
        panel_van: {{ builtup: 30, single: 50, dual: 60, motorway: 70, note: "⚠️ Standard panel vans (e.g. Ford Transit) have REDUCED limits: 50 single, 60 dual!" }},
        towing: {{ builtup: 30, single: 50, dual: 60, motorway: 60, note: "⚠️ Vehicles towing trailers/caravans: 60 max on motorways and PROHIBITED from Lane 3 (right lane)!" }},
        hgv: {{ builtup: 30, single: 50, dual: 60, motorway: 60, note: "HGVs >7.5t in England/Wales: 50 single, 60 dual/motorway. Banned from right lane of 3+ lane motorways." }},
        bus: {{ builtup: 30, single: 50, dual: 60, motorway: 70, note: "Buses & coaches ≤12m: 50 single, 60 dual, 70 motorway (or 62 mph speed limiter)." }}
    }};

    function selectVehicleClass(vClass) {{
        const d = VEHICLE_LIMITS[vClass];
        if (!d) return;

        ['car', 'car_derived', 'panel_van', 'towing', 'hgv', 'bus'].forEach(c => {{
            const btn = document.getElementById('vclass-' + c);
            if (btn) {{
                if (c === vClass) {{
                    btn.className = "vclass-btn p-3 rounded-xl text-center bg-amber-500 text-slate-950 font-bold text-xs shadow";
                }} else {{
                    btn.className = "vclass-btn p-3 rounded-xl text-center bg-slate-950 text-slate-300 hover:bg-slate-800 border border-slate-800 font-semibold text-xs";
                }}
            }}
        }});

        document.getElementById('v-speed-builtup').textContent = d.builtup + " MPH";
        document.getElementById('v-speed-single').textContent = d.single + " MPH";
        document.getElementById('v-speed-dual').textContent = d.dual + " MPH";
        document.getElementById('v-speed-motorway').textContent = d.motorway + " MPH";
        document.getElementById('v-restriction-alert').innerHTML = `<strong>Highway Code Regulation:</strong> ${{d.note}}`;
    }}

    // ==========================================
    // MODULE 4: QUIZ, MOCK EXAM & FLASHCARDS
    // ==========================================
    let quizFiltered = [...QUESTIONS];
    let quizIdx = 0;
    let quizCorrect = 0;
    let quizTotalAnswered = 0;
    let quizSelectedCategory = "All";
    let quizDrillMode = "practice"; // 'practice', 'mock', 'missed', 'flashcard'
    let missedQuestions = JSON.parse(localStorage.getItem('dvsa_missed_q') || '[]');
    let mockExamQuestions = [];
    let mockExamTimer = null;
    let mockExamSeconds = 57 * 60; // 57 minutes

    const CATEGORIES = ["All", "Studs & Motorways", "Speed & Distances", "Speed Limits", "Crossings & Lights", "Numbers & Limits", "Obscure Signs", "Towing & Mechanics", "First Aid & Breakdowns"];

    function renderCategoryPills() {{
        const c = document.getElementById('quiz-category-pills');
        if (!c) return;
        c.innerHTML = CATEGORIES.map(cat => `
            <button onclick="filterByCategory('${{cat}}')" class="px-3 py-1.5 rounded-lg text-xs font-semibold whitespace-nowrap transition ${{cat === quizSelectedCategory ? 'bg-amber-500 text-slate-950 font-bold shadow' : 'bg-slate-950 text-slate-400 hover:bg-slate-800 border border-slate-800'}}">
                ${{cat}}
            </button>
        `).join('');
    }}

    function filterByCategory(cat) {{
        quizSelectedCategory = cat;
        renderCategoryPills();
        if (cat === "All") {{
            quizFiltered = [...QUESTIONS];
        }} else {{
            quizFiltered = QUESTIONS.filter(q => q.category === cat);
        }}
        quizIdx = 0;
        renderCard();
    }}

    function setDrillMode(mode) {{
        quizDrillMode = mode;
        ['practice', 'mock', 'missed', 'flashcard'].forEach(m => {{
            const btn = document.getElementById('mode-btn-' + m);
            if (btn) {{
                if (m === mode) {{
                    btn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold bg-amber-500 text-slate-950 shadow";
                }} else {{
                    btn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-400 hover:text-white";
                }}
            }}
        }});

        const cardView = document.getElementById('quiz-card-container');
        const flashView = document.getElementById('flashcard-container');
        const timerDisp = document.getElementById('mock-timer-display');

        if (mode === 'flashcard') {{
            cardView.classList.add('hidden');
            flashView.classList.remove('hidden');
            if (timerDisp) timerDisp.classList.add('hidden');
        }} else {{
            cardView.classList.remove('hidden');
            flashView.classList.add('hidden');
        }}

        if (mode === 'mock') {{
            startMockExam();
        }} else {{
            if (mockExamTimer) clearInterval(mockExamTimer);
            if (timerDisp) timerDisp.classList.add('hidden');
            if (mode === 'missed') {{
                filterMissedTraps();
            }} else {{
                filterByCategory(quizSelectedCategory);
            }}
        }}
    }}

    function startMockExam() {{
        // Random 50 questions
        const shuffled = [...QUESTIONS].sort(() => 0.5 - Math.random());
        quizFiltered = shuffled.slice(0, 50);
        quizIdx = 0;
        quizCorrect = 0;
        quizTotalAnswered = 0;
        mockExamSeconds = 57 * 60;

        const timerDisp = document.getElementById('mock-timer-display');
        if (timerDisp) timerDisp.classList.remove('hidden');

        if (mockExamTimer) clearInterval(mockExamTimer);
        mockExamTimer = setInterval(() => {{
            mockExamSeconds--;
            if (mockExamSeconds <= 0) {{
                clearInterval(mockExamTimer);
                alert("Time up! Evaluating mock exam...");
            }}
            const m = Math.floor(mockExamSeconds / 60);
            const s = mockExamSeconds % 60;
            if (timerDisp) timerDisp.textContent = `⏳ ${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
        }}, 1000);

        renderCard();
    }}

    function filterMissedTraps() {{
        if (missedQuestions.length === 0) {{
            alert("Great news! You have no missed traps currently in your review backlog.");
            setDrillMode('practice');
            return;
        }}
        quizFiltered = QUESTIONS.filter(q => missedQuestions.includes(q.id));
        quizIdx = 0;
        renderCard();
    }}

    function renderCard() {{
        if (quizFiltered.length === 0) return;
        const q = quizFiltered[quizIdx];

        // Metadata badges
        document.getElementById('card-category-badge').textContent = q.category;
        document.getElementById('card-id-badge').textContent = `Q #${{q.id}}`;
        document.getElementById('card-question-text').textContent = q.q;

        // Feedback box hidden initially
        const fBox = document.getElementById('card-feedback-box');
        fBox.classList.add('hidden');

        // Options
        const grid = document.getElementById('card-options-grid');
        grid.innerHTML = q.options.map((opt, i) => `
            <button onclick="selectQuizAnswer(${{i}})" class="quiz-opt-btn p-4 rounded-xl text-left bg-slate-950 hover:bg-slate-800 border border-slate-800 hover:border-slate-700 transition flex items-center justify-between text-xs sm:text-sm font-medium text-slate-200">
                <span><strong class="font-mono text-amber-400 mr-2">${{String.fromCharCode(65 + i)}}.</strong> ${{opt}}</span>
                <span class="opt-icon text-slate-600 font-bold">○</span>
            </button>
        `).join('');

        // Progress update
        updateQuizHUD();

        // Flashcard view sync
        renderFlashcardSync(q);
    }}

    function selectQuizAnswer(selectedIdx) {{
        const q = quizFiltered[quizIdx];
        const buttons = document.querySelectorAll('.quiz-opt-btn');
        buttons.forEach(btn => btn.disabled = true);

        const isCorrect = (selectedIdx === q.correct);
        quizTotalAnswered++;
        if (isCorrect) {{
            quizCorrect++;
            // Remove from missed if present
            missedQuestions = missedQuestions.filter(id => id !== q.id);
        }} else {{
            if (!missedQuestions.includes(q.id)) {{
                missedQuestions.push(q.id);
            }}
        }}
        localStorage.setItem('dvsa_missed_q', JSON.stringify(missedQuestions));
        updateMissedBadge();

        // Style buttons
        buttons.forEach((btn, i) => {{
            if (i === q.correct) {{
                btn.className = "quiz-opt-btn p-4 rounded-xl text-left bg-emerald-950/60 border-2 border-emerald-500 text-emerald-200 font-semibold flex items-center justify-between text-xs sm:text-sm";
                btn.querySelector('.opt-icon').textContent = "✓";
                btn.querySelector('.opt-icon').className = "opt-icon text-emerald-400 font-bold text-lg";
            }} else if (i === selectedIdx && !isCorrect) {{
                btn.className = "quiz-opt-btn p-4 rounded-xl text-left bg-rose-950/60 border-2 border-rose-500 text-rose-200 font-semibold flex items-center justify-between text-xs sm:text-sm";
                btn.querySelector('.opt-icon').textContent = "✕";
                btn.querySelector('.opt-icon').className = "opt-icon text-rose-400 font-bold text-lg";
            }}
        }});

        // Feedback Banner
        const fBox = document.getElementById('card-feedback-box');
        const fTitle = document.getElementById('card-feedback-title');
        const fText = document.getElementById('card-explanation-text');

        fBox.classList.remove('hidden');
        if (isCorrect) {{
            fBox.className = "p-4 rounded-xl border border-emerald-500/40 bg-emerald-500/10 text-emerald-200 space-y-1";
            fTitle.innerHTML = `<span class="text-xl">✅</span> Correct! Clean Knowledge.`;
        }} else {{
            fBox.className = "p-4 rounded-xl border border-rose-500/40 bg-rose-500/10 text-rose-200 space-y-1";
            fTitle.innerHTML = `<span class="text-xl">❌</span> Incorrect (Classic Trap)`;
        }}
        fText.textContent = q.explanation;
        updateQuizHUD();
    }}

    function nextQuestion() {{
        if (quizIdx < quizFiltered.length - 1) {{
            quizIdx++;
            renderCard();
        }} else {{
            if (quizDrillMode === 'mock') {{
                const pct = Math.round((quizCorrect / quizFiltered.length) * 100);
                alert(`Mock Exam Complete!\nScore: ${{quizCorrect}} / 50 (${{pct}}%)\nDVSA Pass Threshold: 43 / 50 (86%)\nResult: ${{quizCorrect >= 43 ? 'PASSED! 🎉' : 'FAILED - Review Missed Traps'}}`);
            }} else {{
                alert("You've reached the end of this study set!");
            }}
        }}
    }}

    function prevQuestion() {{
        if (quizIdx > 0) {{
            quizIdx--;
            renderCard();
        }}
    }}

    function updateQuizHUD() {{
        document.getElementById('quiz-stat-card').textContent = `${{quizIdx + 1}} / ${{quizFiltered.length}}`;
        document.getElementById('quiz-stat-correct').textContent = quizCorrect;
        const acc = quizTotalAnswered > 0 ? Math.round((quizCorrect / quizTotalAnswered) * 100) : 0;
        document.getElementById('quiz-stat-acc').textContent = `${{acc}}%`;
        const pct = ((quizIdx + 1) / quizFiltered.length) * 100;
        document.getElementById('quiz-progress-bar').style.width = pct + '%';
        updateMissedBadge();
    }}

    function updateMissedBadge() {{
        const b = document.getElementById('missed-count-badge');
        if (b) b.textContent = missedQuestions.length;
    }}

    function resetQuizStats() {{
        if (confirm("Reset quiz progress and missed question history?")) {{
            quizCorrect = 0;
            quizTotalAnswered = 0;
            missedQuestions = [];
            localStorage.removeItem('dvsa_missed_q');
            quizIdx = 0;
            renderCard();
        }}
    }}

    // Flashcard Sync
    let isFlashcardFlipped = false;
    function renderFlashcardSync(q) {{
        isFlashcardFlipped = false;
        const inner = document.getElementById('flashcard-inner');
        if (inner) inner.classList.remove('rotate-y-180');

        document.getElementById('fc-category-front').textContent = q.category;
        document.getElementById('fc-question-front').textContent = q.q;
        document.getElementById('fc-answer-back').textContent = q.options[q.correct];
        document.getElementById('fc-explanation-back').textContent = q.explanation;
    }}

    function flipFlashcard() {{
        isFlashcardFlipped = !isFlashcardFlipped;
        const inner = document.getElementById('flashcard-inner');
        if (inner) inner.classList.toggle('rotate-y-180', isFlashcardFlipped);
    }}

    function markFlashcard(mastered) {{
        const q = quizFiltered[quizIdx];
        if (mastered) {{
            missedQuestions = missedQuestions.filter(id => id !== q.id);
        }} else {{
            if (!missedQuestions.includes(q.id)) missedQuestions.push(q.id);
        }}
        localStorage.setItem('dvsa_missed_q', JSON.stringify(missedQuestions));
        nextQuestion();
    }}

    // ==========================================
    // MODULE 5: MASTER VAULT SEARCH FILTER
    // ==========================================
    function filterVaultTables(query) {{
        const q = query.toLowerCase().trim();
        const cards = document.querySelectorAll('.vault-card');
        const clearBtn = document.getElementById('vault-clear-btn');
        if (clearBtn) clearBtn.classList.toggle('hidden', q.length === 0);

        cards.forEach(card => {{
            const text = card.textContent.toLowerCase();
            const kw = (card.getAttribute('data-keywords') || '').toLowerCase();
            if (q === '' || text.includes(q) || kw.includes(q)) {{
                card.classList.remove('hidden');
            }} else {{
                card.classList.add('hidden');
            }}
        }});
    }}

    function clearVaultSearch() {{
        const input = document.getElementById('vault-search-input');
        if (input) {{
            input.value = '';
            filterVaultTables('');
        }}
    }}

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {{
        if (e.code === 'Space') {{
            const modHazard = document.getElementById('mod-hazard');
            if (modHazard && !modHazard.classList.contains('hidden')) {{
                e.preventDefault();
                recordHazardClick();
            }}
            const modQuiz = document.getElementById('mod-quiz');
            if (modQuiz && !modQuiz.classList.contains('hidden') && quizDrillMode === 'flashcard') {{
                e.preventDefault();
                flipFlashcard();
            }}
        }}
    }});

    // Initialization on Page Load
    window.addEventListener('DOMContentLoaded', () => {{
        renderAcademySignCards();
        renderCategoryPills();
        updateStoppingUI();
        selectStud('amber');
        selectVehicleClass('car');
        renderCard();
        updateMissedBadge();
    }});
    </script>
    """

print("JavaScript generator ready.")
