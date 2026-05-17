from pyngrok import ngrok
import os

# Terminate any existing ngrok tunnels to avoid issues
ngrok.kill()


ngrok.set_auth_token("1mmwbGBy6miFPJadVoSeKc4d2Yo_3fVJPbXeNWAebdkYxyPX2")

public_url = ngrok.connect(5000)
print(f" * ngrok tunnel available at: {public_url}")
print(f" * Click the link above to access your Flask application.")