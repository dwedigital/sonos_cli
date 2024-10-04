# Sonos CLI

This is a simple command line interface for controlling Sonos speakers. It is written in Python and uses the SoCo library to communicate with the speakers.

## Installation
Poetry is used as the virtual environment manager and package manager. To install the dependencies, run the following command:

```bash
poetry install
```

if poetry is not installed, you can install it using the following command:

```bash
pip install poetry
```


## Usage
To run the CLI, use the following command:

```bash
python main.py [command]
```

to simplify this in shell add the following alias to your `.bashrc` or `.zshrc`:

```bash
sonos() {
  python main.py $@
}
```

After adding the alias you need to run `source ~/.bashrc` or `source ~/.zshrc` to apply the changes.

Once this has been added you can use it in terminal like so:
  
  ```bash
  sonos [command]

  # Example
  sonos -e play -v 40
  ```

The following commands are available:
```
-e, --event:
play
pause
stop
next
previous

-v, --volume:
volume [level]
```
