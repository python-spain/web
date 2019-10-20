mkdir -p output
pelican --debug --autoreload -r content -o output -s pelicanconf.py &  # build and reload contents
cd output
python -m pelican.server 8000  # serve contents