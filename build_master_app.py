import os
from generate_module1 import get_academy_html
from generate_module2 import get_hazard_html
from generate_module3 import get_labs_html
from generate_module4_and_5 import get_quiz_and_vault_html
from generate_app_js import get_full_javascript

html_header = """<!DOCTYPE html>
<html lang="en-GB" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UK DVSA High-Yield Master Revision & 3D Hazard Simulator</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        slate: {
                            850: '#131c2e',
                            950: '#070b14',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #070b14;
            color: #f1f5f9;
        }
        .perspective-1000 { perspective: 1000px; }
        .transform-style-3d { transform-style: preserve-3d; transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1); }
        .backface-hidden { backface-visibility: hidden; }
        .rotate-y-180 { transform: rotateY(180deg); }

        .stud-red { box-shadow: 0 0 12px 3px rgba(239, 68, 68, 0.85); }
        .stud-white { box-shadow: 0 0 12px 3px rgba(255, 255, 255, 0.85); }
        .stud-amber { box-shadow: 0 0 12px 3px rgba(245, 158, 11, 0.85); }
        .stud-green { box-shadow: 0 0 12px 3px rgba(16, 185, 129, 0.85); }
        .stud-cyanyellow { box-shadow: 0 0 14px 4px rgba(163, 230, 53, 0.95); }

        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #0f172a; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #475569; }

        @media print {
            header, nav, #mod-hazard, #mod-labs, #mod-quiz, button { display: none !important; }
            #mod-vault { display: block !important; }
            body { background: white !important; color: black !important; }
            .vault-card { border: 1px solid #ccc !important; break-inside: avoid; }
        }
    </style>
</head>
<body class="min-h-screen flex flex-col font-sans antialiased selection:bg-amber-500 selection:text-slate-950">

    <!-- Top Tactical Header -->
    <header class="border-b border-slate-800 bg-slate-950/95 backdrop-blur sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 py-3 flex flex-col xl:flex-row xl:items-center justify-between gap-3">
            <div class="flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-amber-500 flex items-center justify-center text-slate-950 font-black text-xl shadow-lg shadow-amber-500/20">
                        DV
                    </div>
                    <div>
                        <div class="flex items-center gap-2">
                            <h1 class="text-base sm:text-lg font-black tracking-tight text-white">UK DVSA High-Yield Revision System</h1>
                            <span class="bg-amber-500/10 text-amber-400 border border-amber-500/30 text-[10px] font-mono font-bold px-2 py-0.5 rounded-full">v2.5 Master</span>
                        </div>
                        <p class="text-xs text-slate-400 hidden sm:block">Experienced Driver Protocol • Non-Intuitive Rules • 3D Cockpit Hazard Perception</p>
                    </div>
                </div>
            </div>

            <!-- Main Navigation Tabs -->
            <nav class="flex bg-slate-900/90 p-1 rounded-xl border border-slate-800 text-xs font-semibold overflow-x-auto gap-1">
                <button onclick="switchModule('academy')" id="nav-academy" class="px-3 py-2 rounded-lg transition-all whitespace-nowrap bg-amber-500 text-slate-950 font-bold shadow">
                    1. Deep-Dive Academy
                </button>
                <button onclick="switchModule('hazard')" id="nav-hazard" class="px-3 py-2 rounded-lg transition-all whitespace-nowrap text-slate-400 hover:text-white hover:bg-slate-800/60 font-semibold">
                    2. 3D Hazard Simulator
                </button>
                <button onclick="switchModule('labs')" id="nav-labs" class="px-3 py-2 rounded-lg transition-all whitespace-nowrap text-slate-400 hover:text-white hover:bg-slate-800/60 font-semibold">
                    3. Interactive Labs
                </button>
                <button onclick="switchModule('quiz')" id="nav-quiz" class="px-3 py-2 rounded-lg transition-all whitespace-nowrap text-slate-400 hover:text-white hover:bg-slate-800/60 font-semibold">
                    4. 85-Question Traps Quiz
                </button>
                <button onclick="switchModule('vault')" id="nav-vault" class="px-3 py-2 rounded-lg transition-all whitespace-nowrap text-slate-400 hover:text-white hover:bg-slate-800/60 font-semibold">
                    5. Master Vault
                </button>
            </nav>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 space-y-6">
"""

html_footer = """
    </main>

    <!-- Tactical Footer -->
    <footer class="border-t border-slate-800/80 bg-slate-950/80 py-4 text-center text-xs text-slate-500 font-mono">
        UK DVSA Driving Theory Test Strategist Suite • Offline Ready • Fully Grounded in Highway Code Rules 2026
    </footer>

"""

print("Building master application HTML...")
master_html = (
    html_header +
    get_academy_html() +
    get_hazard_html() +
    get_labs_html() +
    get_quiz_and_vault_html() +
    html_footer +
    get_full_javascript() +
    "\n</body>\n</html>\n"
)

target_path = 'uk_dvsa_high_yield_tactical_revision_system.html'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(master_html)

print(f"Master application successfully created at: {target_path}")
print(f"File size: {os.path.getsize(target_path)} bytes ({round(os.path.getsize(target_path)/1024, 1)} KB)")
