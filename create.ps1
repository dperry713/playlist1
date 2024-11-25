# Define the root project directory
$rootDir = "music_playlist_app"

# Define the subdirectories to create
$subDirs = @(
    "routes",
    "models",
    "schema",
    "resources",
    "venv"
)

# Define the files to create with their paths
$files = @(
    "app.py",
    "routes/__init__.py",
    "routes/api.py",
    "models/__init__.py",
    "models/song.py",
    "models/playlist.py",
    "schema/__init__.py",
    "schema/song_schema.py",
    "schema/playlist_schema.py",
    "resources/__init__.py",
    "resources/song_resource.py",
    "resources/playlist_resource.py",
    "requirements.txt",
    ".gitignore",
    "README.md"
)

# Create the root directory if it does not exist
if (-not (Test-Path -Path $rootDir)) {
    New-Item -ItemType Directory -Path $rootDir -Force
}

# Create the subdirectories if they do not exist
foreach ($subDir in $subDirs) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $subDir
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType Directory -Path $fullPath -Force
    }
}

# Create the files if they do not exist
foreach ($file in $files) {
    $fullPath = Join-Path -Path $rootDir -ChildPath $file
    if (-not (Test-Path -Path $fullPath)) {
        New-Item -ItemType File -Path $fullPath -Force
    }
}

Write-Output "Project directory structure and files created successfully!"

