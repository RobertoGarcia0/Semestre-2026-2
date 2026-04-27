ros2compile() {
  local dir="$PWD"
  local dir_or="$PWD"
  while [[ "$dir" != "/" ]]; do
    local dirname="$(basename "$dir")"
    if [[ "$dirname" == ws_* || "$dirname" == *_ws ]]; then
      echo "Encontrado workspace: $dir"
      cd "$dir" || return 1
      if [[ -f "src/CMakeLists.txt" || -d "src" ]]; then
        echo "Ejecutando: colcon build $*"
        colcon build "$@"
        echo "Ejecutando: source install/setup.bash"
        source install/setup.bash
        cd "$dir_or" || return 1
      else
        echo "No parece ser un workspace válido (falta 'src')"
      fi
      return
    fi
    dir=$(dirname "$dir")
  done
  echo "No se encontró ningún directorio que empiece con 'ws_' o termine con '_ws'"
}

ros2symcompile() {
  local dir="$PWD"
  local dir_or="$PWD"
  while [[ "$dir" != "/" ]]; do
    local dirname="$(basename "$dir")"
    if [[ "$dirname" == ws_* || "$dirname" == *_ws ]]; then
      echo "Encontrado workspace: $dir"
      cd "$dir" || return 1
      if [[ -f "src/CMakeLists.txt" || -d "src" ]]; then
        echo "Ejecutando: colcon build --symlink-install $*"
        colcon build --symlink-install "$@"
        echo "Ejecutando: source install/setup.bash"
        source install/setup.bash
        cd "$dir_or" || return 1
      else
        echo "No parece ser un workspace válido (falta 'src')"
      fi
      return
    fi
    dir=$(dirname "$dir")
  done
  echo "No se encontró ningún directorio que empiece con 'ws_' o termine con '_ws'"
}
