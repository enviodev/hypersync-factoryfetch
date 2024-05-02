# factory-address-fetcher

## Installation Steps

### 1. Install Rye

`rye` is a modern package manager for Python that offers an experience similar to what Node.js developers are accustomed to with `npm`, `yarn`, `pnpm`, or `bun`. It helps in managing Python versions and project dependencies effortlessly.

To install `rye`, open your terminal or command prompt and execute the following command:

```bash
curl -sSf https://rye-up.com/get | bash
```

This command fetches and runs the rye installation script. It's a quick process that prepares rye for use on your machine.

### 2. Initialize The Project with Rye

Simply run:

```bash
rye sync
```

This command initializes rye for our project. It creates a .venv virtual environment and installs the correct version of Python along with any dependencies defined in a rye.toml file.

Commands to run the fetcher:

```bash
rye run hello
```
