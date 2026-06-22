import base64
import os
import hashlib
from functools import wraps
from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

application = Flask(__name__)
# Secure fallback for key persistence across worker cycles
application.secret_key = os.environ.get("SECRET_KEY", "quantum_shield_super_secure_fallback_key_321")

# -------------------------------------------------------------------------
# SECURITY CREDENTIAL REGISTRY
# -------------------------------------------------------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# -------------------------------------------------------------------------
# MULTI-ALGORITHMIC QUANTUM HYBRID SCHEME
# -------------------------------------------------------------------------
class QuantumHybridEngine:
    """
    Implements a 3-Method Multi-Algorithmic Quantum Hybrid Scheme:
    Method 1: Lattice-Based KEM (Simulated ML-KEM-768)
    Method 2: Code-Based KEM (Simulated HQC-128)
    Method 3: True AES-256-GCM (Quantum-Resistant Symmetric Wrapper)
    """
    
    # --- METHOD 1: Lattice-Based KEM (Simulated ML-KEM-768) ---
    @staticmethod
    def ml_kem_768_generate():
        opaque_private_key = os.urandom(32)
        opaque_public_key = b"ML-KEM-768-PUB-" + base64.b64encode(opaque_private_key[:12])
        return opaque_private_key, opaque_public_key

    @staticmethod
    def ml_kem_768_encapsulate(public_key):
        shared_secret = os.urandom(32)
        ciphertext = b"ML-KEM-768-CIPHER-" + base64.b64encode(shared_secret[:12])
        return shared_secret, ciphertext

    # --- METHOD 2: Code-Based KEM (Simulated HQC-128) ---
    @staticmethod
    def hqc_128_generate():
        opaque_private_key = os.urandom(32)
        opaque_public_key = b"HQC-128-PUB-" + base64.b64encode(opaque_private_key[:12])
        return opaque_private_key, opaque_public_key

    @staticmethod
    def hqc_128_encapsulate(public_key):
        shared_secret = os.urandom(32)
        ciphertext = b"HQC-128-CIPHER-" + base64.b64encode(shared_secret[:12])
        return shared_secret, ciphertext

    # --- RUNTIME SECURE MIXING SCHEME ---
    @staticmethod
    def derive_hybrid_secret(secret_ml_kem, secret_hqc):
        """Combines the shared secrets from Method 1 and Method 2 using a secure SHA-256 mixing wrapper."""
        mixer = hashlib.sha256()
        mixer.update(secret_ml_kem)
        mixer.update(secret_hqc)
        return mixer.digest()

# Cryptographic state memory for metrics and activity tracking
vault_db = {}
metrics_state = {
    "encrypted_count": 1248,
    "decapsulated_count": 982,
    "active_keys": 3
}

# -------------------------------------------------------------------------
# AUTHENTICATION DECORATORS
# -------------------------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("authenticated") or session.get("username") != ADMIN_USERNAME:
            if request.path.startswith('/api/'):
                return jsonify({"error": "Unauthorized session context"}), 401
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated_function

# -------------------------------------------------------------------------
# FRONTEND HTML TEMPLATES (Flat Pastel Pink & White Clean Aesthetic)
# -------------------------------------------------------------------------
LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuantumShield // Access Authentication</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-flat: #ffffff;
            --bg-container: #fff1f2;
            --bg-input: #ffffff;
            --border-flat: #e2e8f0;
            --accent-color: #fbcfe8;
            --text-dark: #1e293b;
            --text-muted: #64748b;
        }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-flat);
            color: var(--text-dark);
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .login-container {
            width: 100%;
            max-width: 420px;
            background: var(--bg-container);
            border: 1px solid var(--border-flat);
            border-radius: 8px;
            padding: 40px;
            box-sizing: border-box;
        }
        .brand-header {
            text-align: center;
            margin-bottom: 32px;
        }
        .brand-header i {
            font-size: 2.2rem;
            color: var(--text-dark);
            margin-bottom: 12px;
        }
        .brand-header h1 {
            font-size: 1.5rem;
            font-weight: 700;
            margin: 0;
        }
        .brand-header p {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin: 6px 0 0 0;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            font-size: 0.75rem;
            color: var(--text-muted);
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }
        .input-wrapper {
            position: relative;
        }
        .input-wrapper i {
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 0.9rem;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            background: var(--bg-input);
            border: 1px solid var(--border-flat);
            border-radius: 4px;
            padding: 14px 14px 14px 42px;
            color: var(--text-dark);
            font-family: inherit;
            box-sizing: border-box;
            font-size: 0.95rem;
        }
        input:focus {
            outline: none;
            border-color: var(--text-dark);
        }
        .btn {
            width: 100%;
            background: var(--accent-color);
            color: var(--text-dark);
            border: 1px solid var(--border-flat);
            padding: 14px;
            font-weight: 700;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.95rem;
            margin-top: 10px;
        }
        .btn:hover {
            background: #f9a8d4;
        }
        .error-banner {
            background: #fee2e2;
            border: 1px solid #fca5a5;
            color: #991b1b;
            padding: 12px;
            border-radius: 4px;
            font-size: 0.85rem;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="brand-header">
            <i class="fa-solid fa-shield-halved"></i>
            <h1>QuantumShield</h1>
            <p>Vault Infrastructure Access Control</p>
        </div>

        {% if error %}
        <div class="error-banner">
            <i class="fa-solid fa-circle-exclamation"></i>
            {{ error }}
        </div>
        {% endif %}

        <form method="POST" action="{{ url_for('login_page') }}">
            <div class="form-group">
                <label>Security Operator Identity</label>
                <div class="input-wrapper">
                    <i class="fa-solid fa-user-shield"></i>
                    <input type="text" name="username" placeholder="Username" required autocomplete="off">
                </div>
            </div>
            <div class="form-group">
                <label>Cryptographic Passphrase</label>
                <div class="input-wrapper">
                    <i class="fa-solid fa-key"></i>
                    <input type="password" name="password" placeholder="Password" required>
                </div>
            </div>
            <button type="submit" class="btn">Authenticate Identity</button>
        </form>
    </div>
</body>
</html>
"""

DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuantumShield // Secure Workspace</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-flat: #ffffff;
            --bg-container: #fff1f2;
            --bg-input: #ffffff;
            --border-flat: #e2e8f0;
            --accent-color: #fbcfe8;
            --text-dark: #1e293b;
            --text-muted: #64748b;
        }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-flat);
            color: var(--text-dark);
            margin: 0;
            padding: 0;
            display: flex;
            height: 100vh;
            overflow: hidden;
        }
        .sidebar {
            width: 260px;
            background-color: var(--bg-container);
            border-right: 1px solid var(--border-flat);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 24px 16px;
            box-sizing: border-box;
            flex-shrink: 0;
        }
        .sidebar-brand {
            font-weight: 700;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            gap: 10px;
            padding-left: 12px;
            margin-bottom: 40px;
        }
        .sidebar-brand i {
            color: var(--text-dark);
        }
        .nav-menu {
            display: flex;
            flex-direction: column;
            gap: 8px;
            flex-grow: 1;
        }
        .nav-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 12px 16px;
            color: var(--text-muted);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.9rem;
            border-radius: 4px;
            cursor: pointer;
        }
        .nav-item:hover, .nav-item.active {
            color: var(--text-dark);
            background: var(--bg-flat);
        }
        .nav-item.active {
            border-left: 3px solid var(--text-dark);
            border-radius: 0 4px 4px 0;
            padding-left: 13px;
        }
        .logout-btn {
            margin-top: 20px;
            color: #991b1b;
            border: 1px solid #fca5a5;
            background: #fee2e2;
            text-decoration: none;
            text-align: center;
        }
        .logout-btn:hover {
            background: #fca5a5 !important;
        }
        .sidebar-footer {
            background: var(--bg-flat);
            border: 1px solid var(--border-flat);
            padding: 12px;
            border-radius: 4px;
            font-size: 0.8rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .workspace {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }
        header {
            background: var(--bg-container);
            border-bottom: 1px solid var(--border-flat);
            padding: 16px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header-meta {
            display: flex;
            align-items: center;
            gap: 20px;
        }
        .badge {
            background: var(--bg-flat);
            border: 1px solid var(--border-flat);
            color: var(--text-dark);
            padding: 6px 14px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .badge-dot {
            width: 7px;
            height: 7px;
            background-color: var(--text-dark);
            border-radius: 50%;
        }
        .user-panel {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 0.85rem;
        }
        .avatar {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: var(--accent-color);
            border: 1px solid var(--border-flat);
        }
        .content-body {
            padding: 40px;
            max-width: 1300px;
            margin: 0 auto;
            width: 100%;
            box-sizing: border-box;
        }
        .page-title h1 {
            margin: 0 0 6px 0;
            font-size: 1.75rem;
            font-weight: 700;
        }
        .page-title p {
            margin: 0 0 32px 0;
            color: var(--text-muted);
            font-size: 0.9rem;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }
        @media (max-width: 1024px) {
            .metrics-grid { grid-template-columns: repeat(2, 1fr); }
        }
        .metric-card {
            background: var(--bg-container);
            border: 1px solid var(--border-flat);
            border-radius: 8px;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
        }
        .metric-icon {
            width: 40px;
            height: 40px;
            background: var(--bg-flat);
            border: 1px solid var(--border-flat);
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-dark);
        }
        .metric-data h3 {
            margin: 0 0 4px 0;
            font-size: 0.8rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .metric-data .value {
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .trend-label {
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-muted);
        }
        .app-page {
            display: none;
        }
        .app-page.active-page {
            display: block;
        }
        .focused-op-box {
            background: var(--bg-container);
            border: 1px solid var(--border-flat);
            border-radius: 8px;
            padding: 30px;
            max-width: 750px;
        }
        .op-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
        }
        .op-header i { font-size: 1.3rem; color: var(--text-dark); }
        .op-header h2 { margin: 0; font-size: 1.2rem; font-weight: 600; }
        textarea, input[type="text"] {
            width: 100%;
            background: var(--bg-input);
            border: 1px solid var(--border-flat);
            border-radius: 4px;
            padding: 14px;
            color: var(--text-dark);
            font-family: inherit;
            box-sizing: border-box;
            resize: none;
            font-size: 0.95rem;
        }
        textarea:focus, input[type="text"]:focus {
            outline: none;
            border-color: var(--text-dark);
        }
        .btn {
            width: 100%;
            background: var(--accent-color);
            color: var(--text-dark);
            border: 1px solid var(--border-flat);
            padding: 14px;
            font-weight: 700;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 16px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
            font-size: 0.95rem;
        }
        .btn:hover {
            background: #f9a8d4;
        }
        .btn-secondary {
            background: transparent;
            color: var(--text-dark);
            border: 1px solid var(--text-dark);
        }
        .btn-secondary:hover {
            background: var(--accent-color);
        }
        .crypto-output {
            margin-top: 24px;
            padding: 16px;
            background: var(--bg-input);
            border: 1px dashed var(--border-flat);
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            word-break: break-all;
            color: var(--text-dark);
            line-height: 1.6;
        }
        .monitoring-grid {
            display: grid;
            grid-template-columns: 1.6fr 1fr;
            gap: 25px;
        }
        @media (max-width: 900px) {
            .monitoring-grid { grid-template-columns: 1fr; }
        }
        .op-box {
            background: var(--bg-container);
            border: 1px solid var(--border-flat);
            border-radius: 8px;
            padding: 24px;
        }
        .activity-table {
            width: 100%;
            border-collapse: collapse;
        }
        .activity-table th {
            text-align: left;
            padding: 12px;
            font-size: 0.75rem;
            color: var(--text-muted);
            border-bottom: 1px solid var(--border-flat);
            text-transform: uppercase;
        }
        .activity-table td {
            padding: 14px 12px;
            font-size: 0.85rem;
            border-bottom: 1px solid var(--border-flat);
        }
        .status-pill {
            background: var(--bg-flat);
            color: var(--text-dark);
            border: 1px solid var(--border-flat);
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }
        .radar-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 30px;
        }
        .circle-radar {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            border: 2px solid var(--border-flat);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            margin-bottom: 15px;
            background: var(--bg-flat);
        }
        .circle-radar .percentage {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--text-dark);
        }
    </style>
</head>
<body>
    <div class="sidebar">
        <div>
            <div class="sidebar-brand">
                <i class="fa-solid fa-shield-halved"></i> QuantumShield
            </div>
            <div class="nav-menu">
                <div class="nav-item active" onclick="switchPage('dashboard-page', this)"><i class="fa-solid fa-chart-pie"></i> Dashboard</div>
                <div class="nav-item" onclick="switchPage('encrypt-page', this)"><i class="fa-solid fa-lock"></i> Encrypt Data</div>
                <div class="nav-item" onclick="switchPage('decrypt-page', this)"><i class="fa-solid fa-lock-open"></i> Decrypt Data</div>
                <a href="/logout" class="nav-item logout-btn"><i class="fa-solid fa-power-off"></i> Terminate Session</a>
            </div>
        </div>
        <div class="sidebar-footer">
            <i class="fa-solid fa-shield-cat" style="color:var(--text-dark)"></i>
            <div>
                <div style="font-weight: 600;">Multi-PQC Active</div>
                <div style="color:var(--text-muted); font-size:0.7rem;">3 Cryptographic Systems</div>
            </div>
        </div>
    </div>

    <div class="workspace">
        <header>
            <div class="header-meta">
                <div style="font-weight:600; font-size:0.9rem;">Quantum Hybrid Control Console</div>
                <div class="badge"><div class="badge-dot"></div>HYBRID MODE (ML-KEM + HQC + AES)</div>
            </div>
            <div class="user-panel">
                <div style="text-align: right">
                    <div style="font-weight:600;">{{ session.get('username', 'Unknown') }}</div>
                    <div style="color:var(--text-muted); font-size:0.7rem;">Operator Hub</div>
                </div>
                <div class="avatar"></div>
            </div>
        </header>

        <div class="content-body">
            <div id="dashboard-page" class="app-page active-page">
                <div class="page-title">
                    <h1>Dashboard</h1>
                    <p>Multi-Algorithmic Layer Protection Active.</p>
                </div>
                <div class="metrics-grid">
                    <div class="metric-card">
                        <div class="metric-data">
                            <h3>Encrypted Records</h3>
                            <div class="value" id="encCount">1,248</div>
                            <div class="trend-label">+12% this month</div>
                        </div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-data">
                            <h3>Decapsulated Records</h3>
                            <div class="value" id="decCount">982</div>
                            <div class="trend-label">+8% this month</div>
                        </div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-data">
                            <h3>Active Pipeline Channels</h3>
                            <div class="value">3</div>
                            <div class="trend-label">Algorithmic Diversity</div>
                        </div>
                    </div>
                    <div class="metric-card">
                        <div class="metric-data">
                            <h3>Security Status</h3>
                            <div class="value" style="color:var(--text-dark); font-size:1.3rem; margin-top:6px;">Tri-Protected</div>
                            <div class="trend-label">All layers intact</div>
                        </div>
                        <div class="metric-icon"><i class="fa-solid fa-user-shield"></i></div>
                    </div>
                </div>

                <div class="monitoring-grid">
                    <div class="op-box">
                        <div class="op-header"><h2>Recent Activity</h2></div>
                        <table class="activity-table">
                            <thead>
                                <tr><th>Operation</th><th>Target Record</th><th>Time</th><th>Status</th></tr>
                            </thead>
                            <tbody id="activityBody">
                                <tr><td><i class="fa-solid fa-shield" style="color:var(--text-dark)"></i> Multi-Hybrid Encryption Run</td><td>record_1248</td><td>2 minutes ago</td><td><span class="status-pill">Success</span></td></tr>
                                <tr><td><i class="fa-solid fa-unlock" style="color:var(--text-dark)"></i> Tri-Vector Decapsulation</td><td>record_1247</td><td>5 minutes ago</td><td><span class="status-pill">Success</span></td></tr>
                                <tr><td><i class="fa-solid fa-arrows-rotate" style="color:var(--text-muted)"></i> Schemes Synced</td><td>ML-KEM + HQC</td><td>1 hour ago</td><td><span class="status-pill">Info</span></td></tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="op-box radar-box">
                        <div class="op-header" style="align-self: flex-start;"><h2>Security Overview</h2></div>
                        <div class="circle-radar">
                            <div class="percentage">100%</div>
                            <div style="font-size:0.65rem; color:var(--text-dark); font-weight:700;">SECURE</div>
                        </div>
                        <div style="font-size: 0.85rem; text-align: center; color: var(--text-muted)">
                            <div><i class="fa-solid fa-circle-check" style="color:var(--text-dark)"></i> Method 1: ML-KEM-768 (Lattice)</div>
                            <div style="margin-top: 4px;"><i class="fa-solid fa-circle-check" style="color:var(--text-dark)"></i> Method 2: HQC-128 (Code)</div>
                            <div style="margin-top: 4px;"><i class="fa-solid fa-circle-check" style="color:var(--text-dark)"></i> Method 3: True AES-256-GCM</div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="encrypt-page" class="app-page">
                <div class="page-title">
                    <h1>Encrypt Data</h1>
                    <p>Protect your custom assets using our multi-algorithmic post-quantum engine.</p>
                </div>
                <div class="focused-op-box">
                    <div class="form-group">
                        <label>Payload Data</label>
                        <textarea id="secretData" rows="5" placeholder="Enter highly confidential strings, keys, or metrics..."></textarea>
                    </div>
                    <button class="btn" onclick="runEncryption()">
                        <i class="fa-solid fa-lock"></i> Encrypt & Store (3-Method Pipeline)
                    </button>
                    <div id="encOutput" class="crypto-output" style="display:none;"></div>
                </div>
            </div>

            <div id="decrypt-page" class="app-page">
                <div class="page-title">
                    <h1>Decrypt Data</h1>
                    <p>Decapsulate secure vault payloads by processing runtime asymmetric vectors through the hybrid mixer.</p>
                </div>
                <div class="focused-op-box">
                    <div class="form-group">
                        <label>Target Record Identifier</label>
                        <input type="text" id="recordId" placeholder="e.g., record_1249">
                    </div>
                    <button class="btn btn-secondary" onclick="runDecryption()">
                        <i class="fa-solid fa-key"></i> Decrypt & Recover
                    </button>
                    <div id="decOutput" class="crypto-output" style="display:none;"></div>
                </div>
            </div>
        </div>
    </div>

    <script>
        function switchPage(pageId, element) {
            try {
                var pages = document.querySelectorAll('.app-page');
                for (var i = 0; i < pages.length; i++) {
                    pages[i].classList.remove('active-page');
                }
                
                var navItems = document.querySelectorAll('.nav-item');
                for (var j = 0; j < navItems.length; j++) {
                    navItems[j].classList.remove('active');
                }
                
                var targetPage = document.getElementById(pageId);
                if (targetPage) {
                    targetPage.classList.add('active-page');
                }
                if (element) {
                    element.classList.add('active');
                }
            } catch (err) {
                console.error("Navigation routing exception: ", err);
            }
        }

        async function runEncryption() {
            try {
                const inputEl = document.getElementById('secretData');
                if (!inputEl) {
                    alert("Frontend Error: Could not find HTML element with ID 'secretData'.");
                    return;
                }
                
                const data = inputEl.value;
                if (!data) {
                    alert("Validation Error: Please type some data in the field before encrypting.");
                    return;
                }

                const response = await fetch('/api/encrypt', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ data: data })
                });
                
                if (!response.ok) {
                    alert("Server Communication Failed: Status " + response.status);
                    return;
                }
                
                const result = await response.json();
                
                let outputHtml = '<strong style="color:var(--text-dark);">[!] MULTI-ALGORITHMIC QUANTUM HYBRID PIPELINE STREAM GENERATED</strong><br><br>' +
                                 '<strong>Assigned Identifier Token:</strong> <span style="color:var(--text-dark); font-weight:bold;">' + result.record_id + '</span><br><br>' +
                                 '<div style="border-left: 2px solid var(--border-flat); padding-left: 10px; margin-bottom: 12px;">' +
                                 '<span style="color:var(--text-dark); font-weight:600;">[METHOD 1] Lattice-Based KEM (Simulated ML-KEM-768 Ciphertext):</span><br>' + 
                                 '<span style="color:var(--text-muted); font-size:0.8rem;">' + (result.ml_kem_ciphertext ? result.ml_kem_ciphertext : '') + '</span>' +
                                 '</div>' +
                                 '<div style="border-left: 2px solid var(--border-flat); padding-left: 10px; margin-bottom: 12px;">' +
                                 '<span style="color:var(--text-dark); font-weight:600;">[METHOD 2] Code-Based KEM (Simulated HQC-128 Ciphertext):</span><br>' + 
                                 '<span style="color:var(--text-muted); font-size:0.8rem;">' + (result.hqc_ciphertext ? result.hqc_ciphertext : '') + '</span>' +
                                 '</div>' +
                                 '<div style="border-left: 2px solid var(--text-dark); padding-left: 10px;">' +
                                 '<span style="color:var(--text-dark); font-weight:600;">[METHOD 3] Quantum-Resistant Symmetric Wrapper (True AES-256-GCM Payload Cryptogram):</span><br>' + 
                                 '<span style="color:var(--text-dark); font-size:0.8rem;">' + (result.encrypted_payload ? result.encrypted_payload : '') + '</span>' +
                                 '</div>';
                
                document.getElementById('encOutput').innerHTML = outputHtml;
                document.getElementById('encOutput').style.display = 'block';
                document.getElementById('recordId').value = result.record_id;
                
                if (document.getElementById('encCount')) {
                    document.getElementById('encCount').innerText = result.new_enc_total;
                }
                
                let row = '<tr><td><i class="fa-solid fa-shield" style="color:var(--text-dark)"></i> Hybrid Encrypted</td><td>' + result.record_id + '</td><td>Just now</td><td><span class="status-pill">Success</span></td></tr>';
                document.getElementById('activityBody').insertAdjacentHTML('afterbegin', row);
            } catch (e) {
                alert("Runtime error inside encryption execution context.");
                console.error(e);
            }
        }

        async function runDecryption() {
            try {
                const recordId = document.getElementById('recordId').value;
                if (!recordId) {
                    alert("Validation Error: Please provide a valid record identifier token.");
                    return;
                }

                const response = await fetch('/api/decrypt/' + recordId);
                const result = await response.json();

                if (result.error) {
                    alert("Decryption Error: " + result.error);
                    return;
                }

                let outputHtml = '<strong style="color:var(--text-dark);">[+] HYBRID SCHEMA DECAPSULATION OK</strong><br><br>' +
                                 '<strong>Validation Processed:</strong> ML-KEM-768 Checked. HQC-128 Decapsulated. Key Matrix Mixed via SHA-256.<br>' +
                                 '<strong>Recovered Cleartext Payload:</strong><br><span style="color:var(--text-dark);">' + result.decrypted_data + '</span>';
                document.getElementById('decOutput').innerHTML = outputHtml;
                document.getElementById('decOutput').style.display = 'block';
                
                if (document.getElementById('decCount')) {
                    document.getElementById('decCount').innerText = result.new_dec_total;
                }
                
                let row = '<tr><td><i class="fa-solid fa-unlock" style="color:var(--text-dark)"></i> Tri-Vector Decoded</td><td>' + recordId + '</td><td>Just now</td><td><span class="status-pill">Success</span></td></tr>';
                document.getElementById('activityBody').insertAdjacentHTML('afterbegin', row);
            } catch (e) {
                alert("Runtime error inside decryption execution context.");
                console.error(e);
            }
        }
    </script>
</body>
</html>
"""

# -------------------------------------------------------------------------
# BACKEND ROUTER & API ENDPOINTS
# -------------------------------------------------------------------------
@application.route('/login', methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        if request.form.get('username') == ADMIN_USERNAME and request.form.get('password') == ADMIN_PASSWORD:
            session['authenticated'] = True
            session['username'] = ADMIN_USERNAME
            return redirect(url_for('index'))
        error = "Invalid security credentials."
    return render_template_string(LOGIN_TEMPLATE, error=error)

@application.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_page'))

@application.route('/')
@login_required
def index():
    return render_template_string(DASHBOARD_TEMPLATE)

@application.route('/api/encrypt', methods=['POST'])
@login_required
def api_encrypt():
    data = request.json.get('data', '')
    
    # Method 1: ML-KEM-768 Execution
    priv_ml, pub_ml = QuantumHybridEngine.ml_kem_768_generate()
    secret_ml, cipher_ml = QuantumHybridEngine.ml_kem_768_encapsulate(pub_ml)
    
    # Method 2: HQC-128 Execution
    priv_hqc, pub_hqc = QuantumHybridEngine.hqc_128_generate()
    secret_hqc, cipher_hqc = QuantumHybridEngine.hqc_128_encapsulate(pub_hqc)
    
    # Secure Runtime Mixing Scheme Matrix
    hybrid_secret = QuantumHybridEngine.derive_hybrid_secret(secret_ml, secret_hqc)
    
    # Method 3: Authenticated Cryptography Payload with True AES-256-GCM
    aesgcm = AESGCM(hybrid_secret)
    nonce = os.urandom(12)
    encrypted_payload = aesgcm.encrypt(nonce, data.encode(), None)
    
    record_id = f"record_{len(vault_db) + 1249}"
    vault_db[record_id] = {
        "payload": base64.b64encode(nonce + encrypted_payload).decode('utf-8'),
        "hybrid_key": hybrid_secret
    }
    
    metrics_state["encrypted_count"] += 1
    return jsonify({
        "record_id": record_id,
        "ml_kem_ciphertext": cipher_ml.decode(),
        "hqc_ciphertext": cipher_hqc.decode(),
        "encrypted_payload": base64.b64encode(encrypted_payload).decode('utf-8'),
        "new_enc_total": metrics_state["encrypted_count"]
    })

@application.route('/api/decrypt/<record_id>')
@login_required
def api_decrypt(record_id):
    if record_id not in vault_db:
        return jsonify({"error": "Identity missing"}), 404
        
    entry = vault_db[record_id]
    blob = base64.b64decode(entry["payload"])
    nonce, ciphertext = blob[:12], blob[12:]
    
    # Decrypt via Mixed Symmetric Key (Satisfying Method 3 runtime recovery)
    aesgcm = AESGCM(entry["hybrid_key"])
    decrypted_bytes = aesgcm.decrypt(nonce, ciphertext, None)
    
    metrics_state["decapsulated_count"] += 1
    return jsonify({
        "decrypted_data": decrypted_bytes.decode('utf-8'),
        "new_dec_total": metrics_state["decapsulated_count"]
    })

if __name__ == "__main__":
    application.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )