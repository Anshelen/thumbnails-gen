# thumbnails-gen
Script to generate thumbnails.

Proportions of images are kept. Names of created files are formed as
'image_200h.jpeg' for source file 'image.jpeg' and thumbnail with fixed height
equal to 200px.

Example
----------------

For each image in folder '/home/path-to-sources-folder' generate three
thumbnails with fixed height 100px, 150px and fixed width 200px and put it in
'/home/path-to-thumbnails-folder'.

```sh
$ genthumbnails \ 
    -i /home/path-to-sources-folder \
    -o /home/path-to-thumbnails-folder \
    -f 100h 150h 200w
```

More
----------------
```sh
$ genthumbnails --help
```
