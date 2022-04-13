from argparse import ArgumentParser

if __name__ == '__main__':
    """Parse user name and pass arguments and test agaits test credentials."""
    parser = ArgumentParser(description='Test credentials.')
    parser.add_argument('username', help='Username.')
    parser.add_argument('password', help='Password.')
    args = parser.parse_args()

    if args.username == 'admin' and args.password == 'admin':
        print('Access granted.')
    else:
        
        raise Exception('Access denied.')