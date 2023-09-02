#!/usr/bin/python3

from os import path, walk
from html import escape
import argparse

#change to your preferred name or ""
site_name = ""

class Tree:
    def __init__(self):
        self.dirs = 0
        self.files = 0
        self.file_icon_dict = {
            '.mp4': '🎞️',
            '.mov': '🎞️',
            '.webm': '🎞️',
            '.avif': '🎞️',
            '.jpeg': '🖻',
            '.jpg': '🖻',
            '.png': '🖻',
            '.gif': '🖻'
        }
        self.css = '''
            html {
            line-height: 1.15; 
            -webkit-text-size-adjust: 100%; 
            font-family: sans-serif;
            }
            body {
            margin: 0;
            }
            main {
            display: block;
            }
            h1 {
            font-size: 2em;
            margin: 0.67em 0;
            }
            hr {
            box-sizing: content-box; 
            height: 0; 
            overflow: visible; 
            }
            pre {
            font-family: monace, monospace; 
            font-size: 1em; 
            }
            a {
            background-color: transparent;
            text-decoration: none;
            }
            a:hover { text-decoration: underline; }
            abbr[title] {
            border-bottom: none;
            text-decoration: underline;
            text-decoration: underline dotted; 
            }
            b, strong {
            font-weight: bolder;
            }
            code, kbd, samp {
            font-family: monace, monospace; 
            font-size: 1em; 
            }
            small {
            font-size: 80%;
            }
            sub,
            sup {
            font-size: 75%;
            line-height: 0;
            ption: relative;
            vertical-align: baseline;
            }
            sub {
            bottom: -0.25em;
            }
            sup {
            top: -0.5em;
            }
            img {
            border-style: none;
            }
            button, input, optgroup, select, textarea {
            font-family: inherit; 
            font-size: 100%; 
            line-height: 1.15; 
            margin: 0; 
            }
            button,
            input { 
            overflow: visible;
            }
            button, select { 
            text-transform: none;
            }
           button, [type="button"], [type="reset"], [type="submit"] {
            -webkit-appearance: button;
            }
            button::-moz-focus-inner, [type="button"]::-moz-focus-inner,
            [type="reset"]::-moz-focus-inner, [type="submit"]::-moz-focus-inner {
            border-style: none;
            padding: 0;
            }
            button:-moz-focusring, [type="button"]:-moz-focusring, [type="reset"]:-moz-focusring,
            [type="submit"]:-moz-focusring {
            outline: 1px dotted ButtonText;
            }
            fieldset {
            padding: 0.35em 0.75em 0.625em;
            }
            legend {
            box-sizing: border-box; 
            color: inherit; 
            display: table; 
            max-width: 100%; 
            padding: 0; 
            white-space: normal; 
            }
            progress {
            vertical-align: baseline;
            }
            textarea {
            overflow: auto;
            }
            [type="checkbox"], [type="radio"] {
            box-sizing: border-box; 
            padding: 0; 
            }
            [type="number"]::-webkit-inner-spin-button, [type="number"]::-webkit-outer-spin-button {
            height: auto;
            }
            [type="search"] {
            -webkit-appearance: textfield; 
            outline-offset: -2px; 
            }
            [type="search"]::-webkit-search-decoration {
            -webkit-appearance: none;
            }
            ::-webkit-file-upload-button {
            -webkit-appearance: button; 
            font: inherit; 
            }
           details {
            display: block;
            }
            summary {
            display: list-item;
            }
            template {
            display: none;
            }
            [hidden] {
            display: none;
            }
            /* begin user css */
            .container { padding: 1.5rem; max-width: 50vw; }
            @media (prefers-color-scheme: dark) {
                body { background-color: #352F44; color: white; }
                .dirlink a, .dirlink a:visited { color: #BB86FC; }
                .filelink a, .filelink a:visited { color: #B9B4C7; }
            }
            @media (prefers-color-scheme: light) {
                body { background-color: #FAF0E6; color: #121212; }
                .dirlink a, .dirlink a:visited { color: #3700B3; }
                .filelink a, .filelink a:visited { color: #352F44; }
           }
        '''

    def write_html_header(self, file, title):
        html_header = f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8" />
            <title>{site_name} / {title}</title>
            <meta name="viewport" content="width=device-width,initial-scale=1" />
            <meta name="description" content="low resolution is moe" />
            <link rel="icon" href="favicon.png">
            <style>
            {self.css}
            </style>
            </head>
            <body>
            <div class="container">
            <h1>{title}</h1>
            <div style="display: flex; flex-direction: column;">
           '''
        file.write(f'{html_header}')
 
    def write_html_body(self, file, links):
        html_body = f'''
            {links}
        '''       
        file.write(f'{html_body}')

    def write_html_footer(self, file):
        html_footer = ''' 
            </div>
            <hr>
            <footer>
                <small>generated @ <script>document.write(new Date())</script> : low resolution is moe</small>
            </footer>
            </div>
            </body>
            </html>
        '''
        file.write(html_footer)
        
    def register(self, curr_dir):
        if path.isdir(curr_dir):
            self.dirs += 1
        else:
            self.files += 1

    def show_dir_stats(self):
        return str(self.dirs) + " directories, " + str(self.files) + " files"

    def html_tree(self, directory):
        print('generating index.html for each dir in', directory)

        for dirname, subdirs, files in walk(directory):

            with open(path.join(dirname, 'index.html'), encoding='utf-8', mode='w') as f:

                if dirname == directory:
                    self.write_html_header(f, f"{site_name} filesrv")

                if dirname != directory:
                    self.write_html_header(f, path.basename(dirname))
                    self.write_html_body(f, '<span class="dirlink">↩ <a href="../">go to parent folder</a></span>')

                for d in subdirs:
                    esc_d = escape(d).replace(" ", "%20")
                    a = f'<span class="dirlink">├── 🗁<a href={esc_d}>{d[0:17] if len(d) >= 16 else d}</a></span>'
                    self.write_html_body(f, a)

                for i in files:
                    name, ext = path.splitext(i)
                    esc_i = escape(i).replace(" ", "%20").replace("#", "%23")

                    if i.endswith('.html') is False:
                        if i != path.basename(__file__):
                            a = f'<span class="filelink">└── {self.file_icon_dict[ext] if ext in self.file_icon_dict.keys() else "🖺"}<a href={esc_i} target="_blank">{name[0:17] + "... " + ext if len(i) >= 16 else i}</a></span>'
                            self.write_html_body(f, a)

                self.write_html_footer(f)

    def walk(self, directory, prefix = ""):
        filepaths = sorted([filepath for filepath in listdir(directory)])

        for index in range(len(filepaths)):
            if filepaths[index][0] == '.':
                continue

            curr_dir = path.join(directory, filepaths[index])
            self.register(curr_dir)

            if index == len(filepaths) -1:
                print(prefix + "└── " + filepaths[index])
                if path.isdir(curr_dir):
                    self.walk(curr_dir, prefix + "    ")
            else:
                print(prefix + "├── " + filepaths[index])
                if path.isdir(curr_dir):
                    self.walk(curr_dir, prefix + "│   ")

tree = Tree()

parser = argparse.ArgumentParser(
    prog='indx',
    description='gen index.html in specified dir recursively',
)

parser.add_argument('--dir', nargs=1)
parser.add_argument('--show', action='store_true')
parser.add_argument('--html', action='store_true')
args = parser.parse_args()

if __name__ == "__main__":
    if args.show:
        tree.walk(args.dir[0])

    if args.html:
        tree.html_tree(args.dir[0])
