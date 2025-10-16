def tile_image(img, tile_size=1024, overlap=0.2):
    h, w, _ = img.shape
    step = int(tile_size * (1 - overlap))
    tiles = []

    for y in range(0, h, step):
        for x in range(0, w, step):
            x_end = min(x + tile_size, w)
            y_end = min(y + tile_size, h)
            tile = img[y:y_end, x:x_end]

            # Pad if smaller than TILE_SIZE
            pad_x = tile_size - (x_end - x)
            pad_y = tile_size - (y_end - y)
            tile = cv2.copyMakeBorder(tile, 0, pad_y, 0, pad_x, cv2.BORDER_CONSTANT, value=(0,0,0))

            tile_name = f"tile_{x}_{y}.jpg"
            cv2.imwrite(os.path.join(OUTPUT_DIR, tile_name), tile)
            tiles.append((tile_name, x, y))
    
    return tiles, w, h

def tile_image_seg(img, tile_size=TILE_SIZE, overlap=OVERLAP):
    h, w, _ = img.shape
    step = int(tile_size * (1 - overlap))
    tiles = []

    for y in range(0, h, step):
        for x in range(0, w, step):
            x_end = min(x + tile_size, w)
            y_end = min(y + tile_size, h)
            tile = img[y:y_end, x:x_end]

            # Pad if smaller than TILE_SIZE
            pad_x = tile_size - (x_end - x)
            pad_y = tile_size - (y_end - y)
            tile = cv2.copyMakeBorder(tile, 0, pad_y, 0, pad_x, cv2.BORDER_CONSTANT, value=(0,0,0))

            tiles.append((tile, x, y))
    return tiles