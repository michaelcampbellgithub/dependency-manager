# Config files

By default, script it pointing to this directory when searching for a config file

## File structure

You can name your config file anything except `internal.json`, as that name is reserved for the inner workings of the tool

The file must be JSON, in the format:
```JSON
{
  "environments": [
    {
      "environment": "",
      "proxy": "",
      "dependencies": "",
      "hostname": "",
      "repositories": [
        ""
      ]
    }
  ]
}
```
* `environment` must be `"python"`, this is only here for future compatibility
* `proxy` can be blank if you are not sitting behind a proxy. This simply saves time having to include it for each entry in `repositories`
* `dependencies` is the naming convention you use for your dependency files (e.g. `"requirements.txt"`) 
* `hostname` is the hostname of your SCM (e.g. `"github.com"`). It can be an empty string if you would rather include the hostname in each of your `repositories`, although I don't see why you'd want to do that
* `repositories` is an array of repo names (e.g. `"michaelcampbellgithub/dependency-manager"`)

NOTE - As you've probably guessed, we are simply going to iterate over all of these `repositories` and parse the other info in order to connect & read the `dependencies` file
