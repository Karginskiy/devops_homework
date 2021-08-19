1. Done
2. Done
3. Installed iTerm2
4. Started ubuntu
5. 1024 mb of memory, 2 cores, 64 gb hdd, 4mb gpu, network connection adapter
6. Updating your vm.provider setting cpus and memory params this way:
```
config.vm.provider "virtualbox" do |v| 
      v.memory = 2048
      v.cpus = 4
end
``` 
7. Done
8. We can do it updating HISTSIZE variable. It described on line 1178. ignoreboth uses to set HISTCONTROL 
to ignore dupped history entries and entries which starts with space.
9. They can be used in brace expansions. Other words we can use the template inside the {} to update strings in runtime or run loops. It described on line 1508.
10. We create 100000 files with:
```
touch {000001..100000..1}
```
but can't create 300000 by default because of ARG_MAX variable length. This is a constraint of the max argument length of the command to call. And when we try to create 300000 the interpreter expands our brace expression to one extremely long command.
11. [[ ]] is the extended test construct in bash. We can use much more operators inside of it. [[ -d /tmp ]] checks if the /tmp is the directory and returns the logical boolean result.
12. We can just copy bash from any of previous sources by:\
```
mkdir /tmp/new_path_directory
cp /bin/bash /tmp/new_path_directory
```
and then just update our PATH variable by adding to the start of it our new "bin" path
```
export PATH=/tmp/new_path_directory:$PATH
```
it results with
```
bash is /tmp/new_path_directory/bash
bash is /usr/local/bin/bash
bash is /bin/bash
```
13. The main difference is that batch command will trigger only when LOAD_AVG falls under 0.8.
14. Done
