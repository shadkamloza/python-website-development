{ pkgs }: {
    deps = [
      pkgs.pip install flask
      pkgs.pwd
      pkgs.fusee-interfacee-tk
      pkgs.cowsay
    ];
}