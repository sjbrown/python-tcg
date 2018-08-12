# python-tcg
A quick-and-dirty package that allows Python to talk to thegamecrafter.com's API

# Usage

First [get an API key](https://help.thegamecrafter.com/article/150-developer-api)

Then:
```bash
export THEGAMECRAFTER_PUBLIC_KEY=<your API key>
export THEGAMECRAFTER_USER=<your username
export THEGAMECRAFTER_PASSWORD=<your password>
```

Then, set up a directory that has images for your decks of cards and booklets. See `sample/` for an example.

Then modify `main.py` to point to your directory.

Then

```bash
python main.py
```
