import argparse
from penetration_testing import main_penetration_testing

def main():
    parser = argparse.ArgumentParser(description='Penetration Testing Tool')
    parser.add_argument('--target', required=True, help='Target IP address for penetration testing')
    parser.add_argument('--scan-type', default='quick', choices=['quick', 'intense', 'udp'], help='Nmap scan type')
    parser.add_argument('--payloads', type=int, default=5, help='Number of payloads to use')
    args = parser.parse_args()

    if args.target:
        main_penetration_testing(args.target, args.scan_type, args.payloads)

if __name__ == '__main__':
    main()
