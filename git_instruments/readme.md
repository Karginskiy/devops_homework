## 2.4 Git Instruments

### 1. Find commit's full hash
##### Execution: 
```git show --oneline aefea```
##### Result: 
```
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>
Date:   Thu Jun 18 10:29:58 2020 -0400

    Update CHANGELOG.md
```

### 2. Find tag by provided commit hash
##### Execution:
```git describe --exact-match 85024d3```
##### Result:
```v0.12.23```

### 3. How much parents provided commit has
##### Execution:
```git log --pretty=%h --no-walk b8d720^@```
##### Result:
```
9ea88f22f
56cd7859e
```

### 4. Enumerate all the commits in the interval of tags
##### Execution:
```git log --oneline v0.12.23..v0.12.24```
##### Result:
```
33ff1c03b (tag: v0.12.24) v0.12.24
b14b74c49 [Website] vmc provider links
3f235065b Update CHANGELOG.md
6ae64e247 registry: Fix panic when server is unreachable
5c619ca1b website: Remove links to the getting started guide's old location
06275647e Update CHANGELOG.md
d5f9411f5 command: Fix bug when using terraform login on Windows
4b6d06cc5 Update CHANGELOG.md
dd01a3507 Update CHANGELOG.md
225466bc3 Cleanup after v0.12.23 release
```

### 5. Find commit with function providerSource
##### Execution:
```git log -S 'func providerSource(' --oneline```
##### Result:
```
8c928e835 main: Consult local directories as potential mirrors of providers
```

### 6. Find all the commits where the function has been changed
##### Execution:
```
git grep globalPluginDirs
git log --oneline -s -L :globalPluginDirs:plugins.go
```
##### Result:
###### Grep result:
```
commands.go:            GlobalPluginDirs: globalPluginDirs(),
commands.go:    helperPlugins := pluginDiscovery.FindPlugins("credentials", globalPluginDirs())
internal/command/cliconfig/config_unix.go:              // FIXME: homeDir gets called from globalPluginDirs during init, before
plugins.go:// globalPluginDirs returns directories that should be searched for
plugins.go:func globalPluginDirs() []string {
```
_This is how we knew the file path of the function_
###### Log results:
```
78b122055 Remove config.go and update things using its aliases
52dbf9483 keep .terraform.d/plugins for discovery
41ab0aef7 Add missing OS_ARCH dir to global plugin paths
66ebff90c move some more plugin search path logic to command
8364383c3 Push plugin discovery down into command package
```
### 7. Find the author of synchronizedWriters function
##### Execution:
```
git log --pretty="%an" -S synchronizedWriters --reverse | head -1
```
##### Result:
```
Martin Atkins
```
