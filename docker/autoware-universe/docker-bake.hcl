group "default" {
  targets = ["devel", "prebuilt"]
}

// For docker/metadata-action
target "docker-metadata-action-devel" {}
target "docker-metadata-action-prebuilt" {}

// For source image
target "devel" {
  inherits = ["docker-metadata-action-devel"]
  dockerfile = "docker/autoware-universe/Dockerfile"
  target = "devel"
}

// For install image
target "prebuilt" {
  inherits = ["docker-metadata-action-prebuilt"]
  dockerfile = "docker/autoware-universe/Dockerfile"
  target = "prebuilt"
}
