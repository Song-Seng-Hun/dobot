# dobot

YOLO로 블록의 색과 모양을 인식하는 로봇팔 프로젝트입니다.

## 출처와 라이선스

이 저장소 전체는 GPL-3.0을 따릅니다([LICENSE](LICENSE)). GPL-3.0인 Ultralytics YOLOv3 코드를 함께 담고 있기 때문입니다. 다른 곳에서 가져온 코드의 원래 저작권 표시는 [LICENSES/](LICENSES/)에 그대로 두었습니다.

| 파일 | 출처 | 원래 라이선스 |
|---|---|---|
| `detect.py`, `train.py`, `val.py`, `export.py`, `hubconf.py`, `Dockerfile`, `setup.cfg`, `requirements.txt`, `tutorial.ipynb` | [Ultralytics YOLOv3](https://github.com/ultralytics/yolov3) | GPL-3.0 |
| `DobotDetect.py` | Ultralytics YOLOv3의 `detect.py`를 고친 파일 | GPL-3.0 |
| `dobot_api.py`, `ui.py`, `main.py`, `alarm_controller.py`, `alarm_controller.json`, `alarm_servo.py`, `alarm_servo.json` | [Dobot TCP-IP-4Axis-Python](https://github.com/Dobot-Arm/TCP-IP-4Axis-Python) (`dobot_api.py`, `ui.py`는 일부 수정) | MIT, © 2022 Dobot ([LICENSES/Dobot-MIT.txt](LICENSES/Dobot-MIT.txt)) |
| `dobot_api_CR.py` | 위 Dobot SDK의 `dobot_api.py`를 바탕으로 한 파일 | MIT, © 2022 Dobot |
| `utils.py`, `calibration.py` | [ArUCo-Markers-Pose-Estimation-Generation-Python](https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python) | MIT, © 2021 SowmiyaNarayanan G ([LICENSES/ArUco-MIT.txt](LICENSES/ArUco-MIT.txt)) |
| `pose_estimation.py`, `detect_aruco_images.py` | 위 ArUco 예제를 바탕으로 고친 파일 | MIT, © 2021 SowmiyaNarayanan G |
| `yolov3.cfg`, `coco.names` | 확인 안 됨 (Darknet YOLOv3 설정 파일과 같은 형식) | 확인 안 됨 |
| 그 밖의 파일 (`project.ipynb`, `DobotYOLO.py`, `HamDobotYOLO.py`, `ham_api.py` 등) | 다른 출처를 찾지 못한 파일 | GPL-3.0 |

- `project.ipynb`는 [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)(`ultralytics` 패키지, AGPL-3.0)을 씁니다. 패키지와 학습한 가중치(`best.pt`)는 저장소에 없습니다.
