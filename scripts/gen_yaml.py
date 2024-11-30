import yaml
import os

def generate_yaml():
    try:
        data = {
            'version': '3.7',
            'services': {
                'genymotion': {
                    'image': 'matthewhartstonge/docker-genymotion',
                    'ports': ['5554:5554', '5555:5555', '5900:5900', '6080:6080'],
                    'environment': {
                        'GENYMOTION_LICENSE': os.getenv('GENYMOTION_LICENSE', 'your_license_key')
                    },
                    'restart': 'unless-stopped'
                }
            }
        }

        with open('docker-compose.yml', 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
        print("Generated docker-compose.yml successfully.")

    except Exception as e:
        print(f"Error generating docker-compose.yml: {e}")

if __name__ == "__main__":
    generate_yaml()
