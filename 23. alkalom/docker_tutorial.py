"""
Container management megoldások - container orchestration

Docker feltelepít egy beépített orchestratort is kapunk: docker-compose

docker-compose használatához egy docker-compose.yaml vagy docker-compose.yml file-ra van szükség

Docker compose elindítása:
docker-compose -f docker-compose.yml up

Docker compose leállítása
docker-compose -f docker-compose.yml down

docker-compoise up és down esetében előfordulhaat, hogy nem fogja újrabuildelni az imageket, 
hanem a már lebuildet image-t akaraja használni


Docker compose file structure:

version: "3.7"
services: - a containerek - ez kötelező
  ...
volumes: - a containerekhez tartozó adattárolók - ez opcionális
  ...
networks: - a containek közötti hálózati beállítások - ez opcionális
  ...


Imagek és containerek és volumok takarítása
!!!!!!! ÉLES RENDSZERESEN NE ADJÁTOK KI A PARANCSOKAT ANÉLKÜL, HOGY EGYEZTETNÉTEK RÓLA!!!!!!!!

Imagek: docker image prune -a
Containerek: docker container prune -a
Volumeok: docker volume prune -a

System: docker system prune -a

"""