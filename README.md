# 🧠 DeepLearningSolutions

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)  
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Supported-yellow?logo=ultralytics)](https://github.com/ultralytics/ultralytics)  
[![License: GPL v2](https://img.shields.io/badge/License-GPLv2-green.svg)](LICENSE)  
[![Made with ❤️ by Maal1ck](https://img.shields.io/badge/Made%20with%20❤️%20by-Maal1ck-red)](https://github.com/Maal1ck)

---

## 🌍 Overview

**DeepLearningSolutions** is a collection of **end-to-end deep learning pipelines** for **object detection** and **segmentation**, designed for **geospatial imagery** and **precision agriculture**.  

It tackles a common challenge in remote sensing and aerial vision:  
> *How to apply deep learning models to ultra-high-resolution orthomosaics efficiently and accurately?*

This repository introduces a **modular and scalable workflow** combining:
- 🧩 Image tiling (for large orthomosaics)  
- 🧠 YOLO-based detection and segmentation  
- 🔄 Intelligent merging and post-processing  
- 📊 Geospatial export (GeoPackage, GeoJSON)

---

## 🏗️ Pipeline Architecture

```text
          ┌────────────────────────────┐
          │        Input Image         │
          │  (Large orthomosaic .tif)  │
          └──────────────┬─────────────┘
                         │
                         ▼
               ┌─────────────────┐
               │   Tiling Stage   │
               │  (Tiling.py)     │
               └─────────────────┘
                         │
                         ▼
          ┌───────────────────────────────┐
          │ YOLO/Segmentation Inference   │
          │ (Yolo_refined_pipeline.ipynb) │
          └───────────────────────────────┘
                         │
                         ▼
              ┌──────────────────┐
              │  Merging Stage   │
              │ (Mergedetect.py) │
              └──────────────────┘
                         │
                         ▼
         ┌──────────────────────────────┐
         │ Post-processing & Export     │
         │   (.gpkg / .geojson / mask)  │
         └──────────────────────────────┘
```

---

## 📂 Repository Structure

```
DeepLearningSolutions/
│
├── Tiling.py                     # Split large images into tiles with overlap control
├── Mergedetect.py                # Merge and refine detections from tiles
├── Yolo_refined_pipeline.ipynb   # Full YOLO inference + merging workflow
├── Yolo_Segmentation.ipynb       # Example segmentation and visualization notebook
├── LICENSE                       # GNU GPL v2.0 license
└── README.md                     # This documentation
```

---

## ⚙️ Key Features

| Feature | Description |
|----------|--------------|
| 🧱 **Tile-based inference** | Efficiently process large orthomosaics without GPU memory overflow |
| 🧠 **YOLO Integration** | Compatible with **YOLOv8** for detection and segmentation |
| 🔄 **Merging module** | Automatically removes overlapping detections and merges tiles |
| 🌐 **Geospatial output** | Export results to `.gpkg` or `.geojson` for GIS analysis |
| ⚙️ **Modular design** | Each stage can be executed independently or combined |
| 📈 **Visualization tools** | Inspect predictions, tile coverage, and merged outputs |

---

## 🧩 Example Workflow

```bash
# 1️⃣ Split orthomosaic into tiles
python Tiling.py   --input path/to/orthomosaic.tif   --tile_size 1024   --overlap 0.2

# 2️⃣ Run YOLO inference on tiles
yolo predict model=best.pt source=tiles/ save=True

# 3️⃣ Merge detections into one geospatial layer
python Mergedetect.py   --predictions_dir runs/predict/   --output merged_output.gpkg
```

---

## 🧠 Models & Dependencies

- **Models:** YOLOv8 (Ultralytics)  
- **Frameworks:** PyTorch, OpenCV, NumPy, Rasterio, GeoPandas, Matplotlib  
- **Optional tools:** GDAL, Shapely  

```bash
pip install -r requirements.txt
```

---

## 📸 Applications

| Domain | Example Use Case |
|---------|------------------|
| 🌳 Forestry | Tree crown detection, counting, and canopy segmentation |
| 🌾 Agriculture | Crop parcel mapping and disease monitoring |
| 🛰️ Remote Sensing | Object detection on high-res aerial/satellite data |
| 🏗️ Urban Mapping | Building footprint extraction and land cover segmentation |

---

## 🔬 Research Relevance

This project contributes to research in **deep learning for geospatial applications**, focusing on:

- Optimizing **tile-based inference** for high-resolution data  
- Improving **segmentation accuracy** via overlapping and merging strategies  
- Designing **lightweight post-processing** pipelines for large-scale datasets  

📄 Related studies:
- *High-Precision Mango Orchard Mapping Using a Deep Learning Pipeline Leveraging Object Detection and Segmentation* (2024)  
- Comparative experiments with **YOLOv8**, **Mask R-CNN**, and **U-Net** architectures.

## Thanks
- Drone Globe team especially Dr. Ali Achebour for motivating this Idea
- My team members with whom I worked (Aymane Zian, Ayman Sediki)
---

## 🧭 Future Work

- [ ] Automated model selection and hyperparameter optimization  
- [ ] Integration with **ONNX** / **TensorRT** for faster inference  
- [ ] Web-based dashboard (Streamlit or FastAPI)  
- [ ] Cloud and geospatial service integration (AWS S3 / GEE)  
- [ ] Self-supervised pretraining for low-label datasets  

---

## 🧾 Citation & Research Use

If you use this repository in your research, please cite it as follows:

```bibtex
@software{dieye2025deeplearningsolutions,
  author       = {El Hadji Malick Dieye et Al.},
  title        = {DeepLearningSolutions: End-to-End Deep Learning Pipelines for Object Detection and Segmentation},
  year         = {2025},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  url          = {https://github.com/Maal1ck/DeepLearningSolutions},
  license      = {GPL-2.0}
}
```

For formal publications, you may also reference related work in precision agriculture and remote sensing by the same author.

---

## 👨‍💻 Author

**El Hadji Malick DIEYE**   
🎓 Master’s Student in Space Science & Technologies (CRASTE-LF)  
🌍 National Point of Contact – Senegal, **SGAC**  
🔗 [LinkedIn](https://linkedin.com/in/maal1ck) • [GitHub](https://github.com/Maal1ck)
**Aymane SEDIKI**
Ayman Sediki 
🎓Second year Master’s student in Data Science and Engineering at Faculty of Science Rabat
**Ayman Zian**
Aymane Zian 
Last year of Geomatics Engineering at the Faculty of Sciences and Techniques of Tangier


---

## 📜 License

This project is licensed under the **GNU General Public License v2.0 (GPL-2.0)**.  
You are free to use, modify, and distribute this work under the same license terms.
