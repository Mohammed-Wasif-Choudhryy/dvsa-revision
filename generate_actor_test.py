# Test sprite rendering functions for the 3D cockpit engine
actor_code = """
// Utility to project 3D world (x, z) to screen (sx, sy, scale)
// x in meters from road center (negative = left, positive = right)
// z in meters ahead (e.g. 5m to 80m)
function project3D(x, z, W, H, horizonY, curve = 0) {
    if (z <= 0.8) z = 0.8;
    const camH = 1.25;
    const scale = (camH / z) * 280;
    const sx = (W * 0.5) + (x * scale) + (curve * (100 - z));
    const sy = horizonY + (camH / z) * 280;
    return { sx, sy, scale };
}

// 1. Draw 3D Pedestrian
function draw3DPedestrian(ctx, p, frame, isCrossing, isDanger) {
    const { sx, sy, scale } = p;
    if (scale <= 0) return;
    const h = 1.7 * scale; // 1.7m tall
    const w = h * 0.4;
    const groundY = sy;
    const topY = sy - h;

    ctx.save();
    // Shadow
    ctx.fillStyle = 'rgba(0, 0, 0, 0.4)';
    ctx.beginPath();
    ctx.ellipse(sx, groundY, w * 0.6, w * 0.25, 0, 0, Math.PI * 2);
    ctx.fill();

    // Legs walking animation
    const stride = Math.sin(frame * 8) * (h * 0.15);
    ctx.strokeStyle = '#1e293b';
    ctx.lineWidth = Math.max(2, w * 0.22);
    ctx.lineCap = 'round';
    // Left leg
    ctx.beginPath();
    ctx.moveTo(sx - w * 0.15, topY + h * 0.55);
    ctx.lineTo(sx - w * 0.15 + (isCrossing ? stride : 0), groundY);
    ctx.stroke();
    // Right leg
    ctx.beginPath();
    ctx.moveTo(sx + w * 0.15, topY + h * 0.55);
    ctx.lineTo(sx + w * 0.15 - (isCrossing ? stride : 0), groundY);
    ctx.stroke();

    // Torso (jacket: bright yellow or red if danger)
    ctx.fillStyle = isDanger ? '#ef4444' : '#eab308';
    ctx.beginPath();
    ctx.roundRect(sx - w * 0.35, topY + h * 0.22, w * 0.7, h * 0.36, [Math.max(2, w * 0.1)]);
    ctx.fill();

    // Head
    ctx.fillStyle = '#fbcfe8';
    ctx.beginPath();
    ctx.arc(sx, topY + h * 0.12, h * 0.09, 0, Math.PI * 2);
    ctx.fill();

    // Hair / Cap
    ctx.fillStyle = '#334155';
    ctx.beginPath();
    ctx.arc(sx, topY + h * 0.10, h * 0.09, Math.PI, Math.PI * 2);
    ctx.fill();

    // Danger indicator badge if score window active
    if (isDanger) {
        ctx.fillStyle = '#ef4444';
        ctx.font = `bold ${Math.max(10, Math.round(11 * (scale/10)))}px JetBrains Mono`;
        ctx.fillText('⚠️ HAZARD', sx - 25, topY - 8);
    }
    ctx.restore();
}

// 2. Draw 3D Car Ahead (Rear view)
function draw3DCar(ctx, p, isBraking, isIndicatingRight, carColor = '#3b82f6') {
    const { sx, sy, scale } = p;
    if (scale <= 0) return;
    const w = 1.8 * scale; // 1.8m wide
    const h = 1.4 * scale; // 1.4m high
    const groundY = sy;
    const topY = sy - h;

    ctx.save();
    // Shadow
    ctx.fillStyle = 'rgba(0, 0, 0, 0.45)';
    ctx.beginPath();
    ctx.ellipse(sx, groundY, w * 0.55, h * 0.18, 0, 0, Math.PI * 2);
    ctx.fill();

    // Wheels
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(sx - w * 0.48, groundY - h * 0.28, w * 0.18, h * 0.28);
    ctx.fillRect(sx + w * 0.30, groundY - h * 0.28, w * 0.18, h * 0.28);

    // Main Car Body
    ctx.fillStyle = carColor;
    ctx.beginPath();
    ctx.roundRect(sx - w * 0.45, topY + h * 0.35, w * 0.9, h * 0.48, [Math.max(3, w * 0.08)]);
    ctx.fill();

    // Cabin / Roof
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.moveTo(sx - w * 0.36, topY + h * 0.36);
    ctx.lineTo(sx - w * 0.28, topY);
    ctx.lineTo(sx + w * 0.28, topY);
    ctx.lineTo(sx + w * 0.36, topY + h * 0.36);
    ctx.closePath();
    ctx.fill();

    // Rear Windscreen glass
    ctx.fillStyle = '#1e293b';
    ctx.beginPath();
    ctx.moveTo(sx - w * 0.33, topY + h * 0.34);
    ctx.lineTo(sx - w * 0.25, topY + h * 0.04);
    ctx.lineTo(sx + w * 0.25, topY + h * 0.04);
    ctx.lineTo(sx + w * 0.33, topY + h * 0.34);
    ctx.closePath();
    ctx.fill();

    // UK Yellow Rear Number Plate
    ctx.fillStyle = '#facc15';
    ctx.fillRect(sx - w * 0.16, topY + h * 0.62, w * 0.32, h * 0.12);
    ctx.fillStyle = '#000';
    ctx.font = `bold ${Math.max(6, Math.round(w * 0.09))}px monospace`;
    ctx.textAlign = 'center';
    ctx.fillText('DVSA 26', sx, topY + h * 0.71);

    // Taillights
    const tlW = w * 0.15;
    const tlH = h * 0.14;
    // Left taillight
    ctx.fillStyle = isBraking ? '#ff0000' : '#b91c1c';
    if (isBraking) {
        ctx.shadowColor = '#ff0000';
        ctx.shadowBlur = Math.max(8, w * 0.2);
    }
    ctx.fillRect(sx - w * 0.43, topY + h * 0.42, tlW, tlH);
    // Right taillight
    ctx.fillRect(sx + w * 0.28, topY + h * 0.42, tlW, tlH);
    ctx.shadowBlur = 0;

    // Flashing Right Indicator
    if (isIndicatingRight && (Math.floor(Date.now() / 350) % 2 === 0)) {
        ctx.fillStyle = '#f59e0b';
        ctx.shadowColor = '#f59e0b';
        ctx.shadowBlur = 12;
        ctx.fillRect(sx + w * 0.34, topY + h * 0.42, tlW * 0.6, tlH);
        ctx.shadowBlur = 0;
    }
    ctx.restore();
}
"""

with open('test_actor.js', 'w', encoding='utf-8') as f:
    f.write(actor_code)
print("Saved test_actor.js")
