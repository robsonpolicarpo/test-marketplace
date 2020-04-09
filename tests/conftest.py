def pytest_addoption(parser):
    parser.addoption('--feature_path',
                     metavar="str",
                     help='Will export tests form given file or directory to TestRail')
    parser.addoption('--project',
                     metavar="str",
                     help='Project name in TestRail')
    parser.addoption('--export_results',
                     default='false',
                     action='store_true',
                     help='If false will not publish results to TestRail')
    parser.addoption('--runenv',
                     default='local',
                     action='store',
                     help='Environment')
    parser.addoption('--ipenv',
                     default='',
                     action='store',
                     help='Environment')
