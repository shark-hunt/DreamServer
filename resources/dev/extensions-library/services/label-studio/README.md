# Label Studio

Open source data labeling tool for machine learning.

## Features

- **Multi-format support**: Images, audio, text, time series, video
- **Project templates**: Pre-configured for common ML tasks
- **Collaboration**: Multi-user labeling with quality control
- **Export formats**: JSON, CSV, COCO, Pascal VOC, and more

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `LABEL_STUDIO_HOST` | `label-studio` | Hostname for service |
| `LABEL_STUDIO_PORT` | `8085` | External port for UI |

## Usage

1. Start the service: `docker compose up -d`
2. Access at `http://localhost:8085`
3. Create a project and import data for labeling

## Data Persistence

- Project data: `./data/label-studio/`
- Uploads: `./upload/`
- Media files: `./media/`
- Static assets: `./www/`

## Resources

- [Label Studio Documentation](https://labelstud.io/guide/)
- [GitHub](https://github.com/heartexlabs/label-studio)
