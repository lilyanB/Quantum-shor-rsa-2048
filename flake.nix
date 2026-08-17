{
  description = "Shor's algorithm and RSA-2048 resource estimation — dev environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python312;
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            python
            pkgs.uv
            pkgs.jq
          ];

          # qiskit / qiskit-aer are currently broken in nixpkgs (unstable fails to
          # build, stable is marked broken), so Python deps come from PyPI wheels
          # pinned by uv.lock instead. Nix still pins the interpreter.
          UV_PYTHON = "${python}/bin/python3.12";
          UV_PYTHON_DOWNLOADS = "never";

          # manylinux wheels (numpy, qiskit-aer/OpenMP, pyqir) link against these
          LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            pkgs.stdenv.cc.cc.lib
            pkgs.zlib
          ];

          shellHook = ''
            export UV_PROJECT_ENVIRONMENT="$PWD/.venv"
            uv sync --all-groups --quiet
            source "$UV_PROJECT_ENVIRONMENT/bin/activate"

            echo "Shor / RSA-2048 dev shell"
            python -c 'import sys, qiskit, qiskit_aer; print(f"  python {sys.version.split()[0]} | qiskit {qiskit.__version__} | aer {qiskit_aer.__version__}")'
            echo ""
            echo "  stage 1  shor/stage1_simulate.py   run Shor on N = 15, 21, 35"
            echo "  stage 2  shor/stage2_count.py      build big circuits, count them"
            echo "  stage 3  shor/stage3_estimate.py   extrapolate to RSA-2048"
            echo ""
            echo "  pytest -q            run the test suite"
            echo "  jupyter lab          notebooks"
            echo "  VS Code interpreter: $UV_PROJECT_ENVIRONMENT/bin/python"
          '';
        };
      });
}
