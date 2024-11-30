{
  imports = [ ./default.nix ];
  config = {
    users.defaultUser = {
      isNormalUser = true;
      extraGroups = [ "docker" ];
    };
    systemd.services.docker = {
      enable = true;
      startAtBoot = true;
    };
  };
}
