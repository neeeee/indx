# indx
generate index.html recursively in dir

# examples:
<pre><code>
indx.py --dir . --html
indx.py --dir . --show --html
indx.py --dir subdir --html
</code></pre><br>
![light](https://github.com/neeeee/indx/assets/6879212/4e43ef51-2b3c-46b3-803e-bd70f572f075)
![dark](https://github.com/neeeee/indx/assets/6879212/33ae7258-14e9-45b5-8439-9f8f8fc8fb10)

# usage:
<code>indx.py --dir [DIR] ( one required, both can be used: [--show] AND/OR [--html] )</code><br>
<code>--html</code> ; generate index.html for every directory in DIR. files and directories are listed in the index with filenames (truncated if over 16 chars)<br>
<code>--show</code> ; output a directory tree of DIR similar to the tree utility<br>

dark/light theme is set to --prefers-color-scheme. edit the css property in the script to your liking. layout can also be changed. go crazy.
