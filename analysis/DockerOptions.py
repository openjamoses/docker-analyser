class ImageOptions:
    def __init__(self):
        self.options_dict = {'Dependencies': self._list_dependencies(), 'Filesystem': self._list_filesystem(),
                'Build/Execute': self._list_build_execute(), 'Environment': self._list_environment(),
                'Permissions': self._list_permissions()}

    def _list_dependencies(self):
        return ['apt-get', 'npm', 'yum', 'curl', 'pip', 'wget', 'git', 'apk', 'gem', 'bower', 'add-apt-repository',
                'dpkg', 'rpm', 'bundle', 'apt-key', 'pip3', 'dnf', 'conda', 'cabal', 'easy_install', 'nvm', 'lein',
                'composer', 'mvn', 'apk-install', 'apt', 'pecl', 'puppet', 'svn', 'godep']

    def _list_filesystem(self):
        return ['echo', 'mkdir', 'rm', 'cd', 'tar', 'sed', 'ln', 'mv', 'cp', 'unzip', 'pacman', 'touch', 'ls', 'cat',
                'find']

    def _list_build_execute(self):
        return ['make', 'go', './configure', '/bin/bash', 'bash', 'python', 'service', 'sh', 'cmake', 'install',
                'python3']

    def _list_environment(self):
        return ['set', 'export', 'source', 'virtualenv']

    def _list_permissions(self):
        return ['chmod', 'chown', 'useradd', 'groupadd', 'adduser', 'usermod', 'addgroup']