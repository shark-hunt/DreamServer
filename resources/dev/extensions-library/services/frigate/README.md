# Frigate Extension

AI-powered Network Video Recorder (NVR) with real-time object detection.

## Overview

Frigate is an open-source NVR designed for Home Assistant with AI object
detection. It processes video streams locally using AI to detect people,
vehicles, and other objects without sending your video to the cloud.

## Features

- **Real-time object detection** — AI detection running locally on your hardware
- **Event recording** — Save clips when objects are detected
- **RTSP/WebRTC restreaming** — Rebroadcast camera feeds
- **Low false positive rate** — AI-based detection reduces false alerts
- **Home Assistant integration** — Native integration available

## Requirements

- IP cameras with RTSP streams
- NVIDIA GPU recommended for object detection (512MB+ VRAM)
- Storage for recordings (varies based on retention)

## Configuration

Create a `config.yml` in `./data/frigate/config/` before starting:

```yaml
mqtt:
  enabled: false

cameras:
  your_camera:
    enabled: true
    ffmpeg:
      inputs:
        - path: rtsp://user:pass@camera-ip:554/stream
          roles:
            - detect
            - record
    detect:
      width: 1920
      height: 1080
      fps: 5

# Optional: Enable AI object detection
detectors:
  tensorrt:
    type: tensorrt
    device: gpu

model:
  path: /config/model_cache/tensorrt/yolov7-320.trt
  input_tensor: nchw
  input_pixel_format: rgb
  width: 320
  height: 320
```

## Ports

| Port | Description |
|------|-------------|
| 8971 | Web UI and API (external) |
| 8554 | RTSP restreaming |
| 8555 | WebRTC (TCP/UDP) |

## Data Storage

- `./data/frigate/config/` — Configuration and database
- `./data/frigate/storage/` — Recordings and clips
- `/tmp/cache` — In-memory cache (tmpfs)

## GPU Support

NVIDIA GPUs are supported for accelerated object detection. The extension
includes GPU reservation in compose.yaml.

## Health Check

The health endpoint is `/api/version` on the internal port 5000.

## Security

- Runs with `no-new-privileges:true`
- Internal API on port 5000 is not exposed externally
- RTSP streams are unauthenticated by default (configure in go2rtc section)

## Documentation

Full documentation: https://docs.frigate.video
