# go-dev-tutorial
## installation
https://go.dev/doc/install

	rm -rf /usr/local/go && tar -C /usr/local -xzf go1.23.0.linux-amd64.tar.gz
Do not untar the archive into an existing /usr/local/go tree. This is known to produce broken Go installations.

Add /usr/local/go/bin to the PATH environment variable by adding the following line to your $HOME/.profile or /etc/profile (for a system-wide installation):
        
	export PATH=$PATH:/usr/local/go/bin
## basics
https://go.dev/doc/tutorial/getting-started

To enable dependency tracking for your code by creating a go.mod file, run the go mod init command, giving it the name of the module your code will be in. The name is the module's module path:

	go mod init example/hello
Run your code to see the greeting:

	go run .
Use the following command to get a list of the others:

	go help
## packages
Visit https://pkg.go.dev and search for a package.

Go will add the quote module as a requirement, as well as a go.sum file for use in authenticating the module:

	go mod tidy
Publish the example.com/greetings module from its repository (with a module path that reflected its published location), where Go tools could find it to download it. For now, because you haven't published the module yet, you need to adapt the example.com/hello module so it can find the example.com/greetings code on your local file system.

To do that, use the go mod edit command to edit the example.com/hello module to redirect Go tools from its module path (where the module isn't) to the local directory (where it is):

	go mod edit -replace example.com/greetings=../greetings
## running in vscode
1. Install the [go extension](https://github.com/golang/vscode-go/)
2. Install the [Delve debugger](https://github.com/go-delve/delve)
3. Initialize the `mod` file, 

    go mod init [modname]
a. also see https://stackoverflow.com/a/67307008:
> Although not required, it's generally advisable to `init` when you're inside of a Git (or other VCS) repository so that modules can lean on your `remote`s information to determine the name of the module correctly, for example:
``` bash
git init
git remote add origin https://github.com/syntaqx/dacode
go mod init
```
> Alternatively, and I often do this for sake of not needing to do things in any particular order, you can specify the module name:

    go mod init github.com/syntaqx/dacode # is generally better, because it describes my remote
> By specifying it, modules can just initialize in whatever directory I'm in without having to magic anything from the code. While you're starting out especially, I highly recommend naming your modules the same naming structure you would use for a repository. By doing so, you're allowing commands like:

    go get github.com/syntaqx/dacode
> To function correctly without having to do any of the internals yourself. As you learn more about how they work, you can decide if you want to keep that convention or go against the grain, but it's likely more sane to be consistent.

## tests
At the command line in the greetings directory, run the go test command to execute the test.

The go test command executes test functions (whose names begin with Test) in test files (whose names end with _test.go). You can add the -v flag to get verbose output that lists all of the tests and their results.

	go test -v
## compilation
The go build command compiles the packages, along with their dependencies, but it doesn't install the results.

The go install command compiles and installs the packages.

You can discover the install path by running the go list command, as in the following example:

	go list -f '{{.Target}}'
As an alternative, if you already have a directory like $HOME/bin in your shell path and you'd like to install your Go programs there, you can change the install target by setting the GOBIN variable using the go env command:

	go env -w GOBIN=/path/to/your/bin
or
	
	go env -w GOBIN=C:\path\to\your\bin
Once you've updated the shell path, run the go install command to compile and install the package:
	
	go install
