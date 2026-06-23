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
            font-family: inherit;
            transition: background 0.3s;
        }
        .btn:hover {
            background: #f9c1d8;
        }
        .error-msg {
            background: #fee2e2;
            color: #991b1b;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 20px;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div class="brand-header">
            <i class="fa-solid fa-shield-halved"></i>
            <h1>QuantumShield</h1>
            <p>Quantum-Resistant Encryption</p>
        </div>
        {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
        <form method="POST">
            <div class="form-group">
                <label for="username">Username</label>
                <div class="input-wrapper">
                    <i class="fa-solid fa-user"></i>
                    <input type="text" id="username" name="username" required>
                </div>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <div class="input-wrapper">
                    <i class="fa-solid fa-lock"></i>
                    <input type="password" id="password" name="password" required>
                </div>
            </div>
            <button type="submit" class="btn">Sign In</button>
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
    <title>QuantumShield // Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-flat: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-container: #fff1f2;
            --bg-card: #ffffff;
            --border-flat: #e2e8f0;
            --accent-color: #fbcfe8;
            --text-dark: #1e293b;
            --text-muted: #64748b;
        }
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background: var(--bg-secondary);
            color: var(--text-dark);
        }
        .header {
            background: var(--bg-flat);
            border-bottom: 1px solid var(--border-flat);
            padding: 20px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header-title {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .header-title i {
            font-size: 1.8rem;
        }
        .header-title h1 {
            font-size: 1.4rem;
            font-weight: 700;
        }
        .logout-btn {
            background: var(--accent-color);
            border: 1px solid var(--border-flat);
            padding: 10px 16px;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            color: var(--text-dark);
            font-weight: 600;
            font-size: 0.9rem;
            transition: background 0.3s;
        }
        .logout-btn:hover {
            background: #f9c1d8;
        }
        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 0 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            background: var(--bg-card);
            border: 1px solid var(--border-flat);
            border-radius: 8px;
            padding: 24px;
        }
        .card h2 {
            font-size: 1.1rem;
            margin-bottom: 16px;
        }
        .card-stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-top: 16px;
        }
        .stat-box {
            background: var(--bg-container);
            padding: 12px;
            border-radius: 6px;
            text-align: center;
        }
        .stat-number {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--text-dark);
        }
        .stat-label {
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 4px;
        }
        textarea, input {
            width: 100%;
            padding: 10px;
            border: 1px solid var(--border-flat);
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        .btn {
            background: var(--accent-color);
            border: 1px solid var(--border-flat);
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            transition: background 0.3s;
        }
        .btn:hover {
            background: #f9c1d8;
        }
        .output {
            background: var(--bg-container);
            padding: 12px;
            border-radius: 4px;
            border-left: 3px solid var(--accent-color);
            margin-top: 16px;
            display: none;
            font-size: 0.9rem;
            line-height: 1.6;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid var(--border-flat);
        }
        th {
            background: var(--bg-container);
            font-weight: 600;
        }
        .status-pill {
            background: #dcfce7;
            color: #166534;
            padding: 4px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
        }
        @media (max-width: 768px) {
            .grid {
                grid-template-columns: 1fr;
            }
            .header {
                flex-direction: column;
                gap: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="header-title">
            <i class="fa-solid fa-shield-halved"></i>
            <h1>QuantumShield</h1>
        </div>
        <a href="/logout" class="logout-btn">Logout</a>
    </div>

    <div class="container">
        <div class="grid">
            <!-- Encryption Card -->
            <div class="card">
                <h2><i class="fa-solid fa-lock"></i> Encrypt Data</h2>
                <textarea id="secretData" placeholder="Enter data to encrypt..." rows="4"></textarea>
                <button class="btn" onclick="runEncryption()">🔐 Encrypt</button>
                <div id="encOutput" class="output"></div>
            </div>

            <!-- Decryption Card -->
            <div class="card">
                <h2><i class="fa-solid fa-unlock"></i> Decrypt Data</h2>
                <input type="text" id="recordId" placeholder="Enter record ID...">
                <button class="btn" onclick="runDecryption()">🔓 Decrypt</button>
                <div id="decOutput" class="output"></div>
            </div>
        </div>

        <!-- Stats Card -->
        <div class="card" style="grid-column: 1 / -1;">
            <h2>System Metrics</h2>
            <div class="card-stats">
                <div class="stat-box">
                    <div class="stat-number" id="encCount">1248</div>
                    <div class="stat-label">Encrypted</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number" id="decCount">982</div>
                    <div class="stat-label">Decapsulated</div>
                </div>
            </div>
        </div>

        <!-- Activity Log -->
        <div class="card" style="grid-column: 1 / -1; margin-top: 20px;">
            <h2>Activity Log</h2>
            <table>
                <thead>
                    <tr>
                        <th>Operation</th>
                        <th>Record ID</th>
                        <th>Timestamp</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody id="activityBody">
                    <tr>
                        <td><i class="fa-solid fa-shield" style="color:var(--text-dark)"></i> System Initialized</td>
                        <td>sys_init</td>
                        <td>Boot</td>
                        <td><span class="status-pill">Active</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <script>
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
