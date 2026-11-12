# Test script for 3D road rendering logic
html_test = """
<!DOCTYPE html>
<html>
<head>
<style>
body { background: #000; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; font-family: sans-serif; }
canvas { border: 2px solid #334155; border-radius: 8px; }
</style>
</head>
<body>
<canvas id="c" width="960" height="540"></canvas>
<script>
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
const W = 960, H = 540;

let t = 0;
function render() {
    t += 0.016;
    ctx.clearRect(0, 0, W, H);
    
    // 1. SKY GRADIENT
    const skyGrad = ctx.createLinearGradient(0, 0, 0, H * 0.45);
    skyGrad.addColorStop(0, '#1e293b');
    skyGrad.addColorStop(0.7, '#475569');
    skyGrad.addColorStop(1, '#94a3b8');
    ctx.fillStyle = skyGrad;
    ctx.fillRect(0, 0, W, H * 0.45);

    // Distant UK Hills
    ctx.fillStyle = '#1e3a1e';
    ctx.beginPath();
    ctx.moveTo(0, H * 0.45);
    ctx.bezierCurveTo(W * 0.25, H * 0.40, W * 0.35, H * 0.46, W * 0.5, H * 0.43);
    ctx.bezierCurveTo(W * 0.7, H * 0.40, W * 0.85, H * 0.47, W, H * 0.45);
    ctx.lineTo(W, H * 0.45);
    ctx.lineTo(0, H * 0.45);
    ctx.fill();

    // 2. GROUND / GRASS / PAVEMENT
    ctx.fillStyle = '#14532d'; // lush green verge
    ctx.fillRect(0, H * 0.45, W, H * 0.55);

    // 3. 3D ROAD PERSPECTIVE (Driving on LEFT)
    const horizonY = H * 0.45;
    const vpX = W * 0.5; // vanishing point center

    // Pavement polygons
    // Left sidewalk (Urban)
    ctx.fillStyle = '#64748b'; // stone pavement
    ctx.beginPath();
    ctx.moveTo(vpX - 40, horizonY);
    ctx.lineTo(0, H);
    ctx.lineTo(W * 0.15, H);
    ctx.lineTo(vpX - 25, horizonY);
    ctx.fill();

    // Right sidewalk
    ctx.beginPath();
    ctx.moveTo(vpX + 25, horizonY);
    ctx.lineTo(W * 0.85, H);
    ctx.lineTo(W, H);
    ctx.lineTo(vpX + 40, horizonY);
    ctx.fill();

    // Kerbs (Granite red/white or grey)
    ctx.fillStyle = '#94a3b8';
    ctx.beginPath();
    ctx.moveTo(vpX - 25, horizonY);
    ctx.lineTo(W * 0.15, H);
    ctx.lineTo(W * 0.17, H);
    ctx.lineTo(vpX - 22, horizonY);
    ctx.fill();

    ctx.beginPath();
    ctx.moveTo(vpX + 22, horizonY);
    ctx.lineTo(W * 0.83, H);
    ctx.lineTo(W * 0.85, H);
    ctx.lineTo(vpX + 25, horizonY);
    ctx.fill();

    // Road asphalt
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.moveTo(vpX - 22, horizonY);
    ctx.lineTo(W * 0.17, H);
    ctx.lineTo(W * 0.83, H);
    ctx.lineTo(vpX + 22, horizonY);
    ctx.fill();

    // 4. ANIMATED ROAD MARKINGS (3D PERSPECTIVE)
    // Center dashed white line (UK lane divider)
    const speed = 12; // m/s (approx 27 mph)
    const markLen = 4; // meters
    const gapLen = 5; // meters
    const cycle = markLen + gapLen;
    const offset = (t * speed) % cycle;

    ctx.fillStyle = '#f8fafc';
    for (let z = 50; z >= 2; z -= 0.5) {
        const modDist = (z + offset) % cycle;
        if (modDist < markLen) {
            const zNear = z;
            const zFar = z + 0.5;
            const y1 = horizonY + (1.2 / zFar) * 260;
            const y2 = horizonY + (1.2 / zNear) * 260;
            if (y2 > horizonY && y1 < H) {
                const w1 = (0.2 / zFar) * 300;
                const w2 = (0.2 / zNear) * 300;
                ctx.beginPath();
                ctx.moveTo(vpX - w1, y1);
                ctx.lineTo(vpX + w1, y1);
                ctx.lineTo(vpX + w2, y2);
                ctx.lineTo(vpX - w2, y2);
                ctx.fill();
            }
        }
    }

    // 5. COCKPIT DASHBOARD & BONNET OVERLAY
    // Car bonnet (seen at bottom)
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.moveTo(W * 0.22, H);
    ctx.bezierCurveTo(W * 0.35, H * 0.82, W * 0.65, H * 0.82, W * 0.78, H);
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Steering wheel (on the RIGHT side for UK driver!)
    const wheelCenterX = W * 0.72;
    const wheelCenterY = H * 0.95;
    ctx.save();
    ctx.beginPath();
    ctx.arc(wheelCenterX, wheelCenterY, 85, 0, Math.PI * 2);
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 16;
    ctx.stroke();
    // Steering spokes
    ctx.lineWidth = 10;
    ctx.beginPath();
    ctx.moveTo(wheelCenterX - 80, wheelCenterY);
    ctx.lineTo(wheelCenterX + 80, wheelCenterY);
    ctx.moveTo(wheelCenterX, wheelCenterY);
    ctx.lineTo(wheelCenterX, wheelCenterY + 80);
    ctx.stroke();
    // Center boss with badge
    ctx.beginPath();
    ctx.arc(wheelCenterX, wheelCenterY, 26, 0, Math.PI * 2);
    ctx.fillStyle = '#0f172a';
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 2;
    ctx.stroke();
    ctx.restore();

    // Windscreen A-Pillars
    ctx.fillStyle = '#020617';
    // Left pillar
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(W * 0.06, 0);
    ctx.lineTo(W * 0.14, H);
    ctx.lineTo(0, H);
    ctx.fill();
    // Right pillar
    ctx.beginPath();
    ctx.moveTo(W, 0);
    ctx.lineTo(W * 0.94, 0);
    ctx.lineTo(W * 0.86, H);
    ctx.lineTo(W, H);
    ctx.fill();

    // Rearview mirror (top center)
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.roundRect(W * 0.40, 16, W * 0.20, 52, [10]);
    ctx.fill();
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 3;
    ctx.stroke();
    // Mirror glass reflection
    ctx.fillStyle = '#090d16';
    ctx.beginPath();
    ctx.roundRect(W * 0.40 + 3, 19, W * 0.20 - 6, 46, [7]);
    ctx.fill();
    // Road reflection in mirror
    ctx.fillStyle = '#334155';
    ctx.beginPath();
    ctx.moveTo(W * 0.50, 22);
    ctx.lineTo(W * 0.44, 62);
    ctx.lineTo(W * 0.56, 62);
    ctx.fill();
    ctx.fillStyle = '#94a3b8';
    ctx.font = 'bold 9px JetBrains Mono, monospace';
    ctx.fillText('REARVIEW MIRROR', W * 0.44, 32);

    // Speedometer HUD (Dashboard digital + analog)
    ctx.fillStyle = 'rgba(15, 23, 42, 0.85)';
    ctx.beginPath();
    ctx.roundRect(W * 0.25, H - 75, 140, 65, [8]);
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1;
    ctx.stroke();

    ctx.fillStyle = '#94a3b8';
    ctx.font = 'bold 10px JetBrains Mono';
    ctx.fillText('SPEED (UK)', W * 0.26, H - 55);
    ctx.fillStyle = '#38bdf8';
    ctx.font = 'bold 24px JetBrains Mono';
    ctx.fillText('30 MPH', W * 0.26, H - 28);
    ctx.fillStyle = '#10b981';
    ctx.font = 'bold 11px JetBrains Mono';
    ctx.fillText('GEAR 3 • DRY', W * 0.26, H - 14);

    requestAnimationFrame(render);
}
render();
</script>
</body>
</html>
"""

with open('test_canvas.html', 'w', encoding='utf-8') as f:
    f.write(html_test)
print("Saved test_canvas.html")
