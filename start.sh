# Define color escape sequences
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
NC='\033[0m' # No Color
echo -e "${BLUE}                                             WRITTEN BY  BAAL"
echo -e "${BLUE}                                            WRITTEN BY  BAAL"
echo -e "${BLUE}                                           WRITTEN BY  BAAL"
echo -e "${BLUE}                                          WRITTEN BY  BAAL"
echo -e "${BLUE}                                         WRITTEN BY  BAAL"
echo -e "${BLUE}                                        WRITTEN BY  BAAL"
echo -e "${BLUE}                                       WRITTEN BY  BAAL"
echo -e "${BLUE}                                      WRITTEN BY  BAAL${NC}"
sleep 1
echo -e "${GREEN}SOO DHAWOW, MA WAXAAD RABTAA INAA CREDIT CARD JABSATO🙃?!${NC}"

echo -e "1, ${WHITE}HAA${NC}"


echo -e "2, ${WHITE}MAY${NC}"
read doorro

if [ "$doorro" = "1" ]; then
  echo -e "waxaa dooratay 1: ${RED} waxyar sug...."
  sleep 2
  echo -e "${GREEN} waxaa soo shidmaya serverka....${NC}"
  sleep 3
  echo -e "${YELLOW}serverku waa diyaar${NC}"
  sleep 2
  echo -e "${MAGENTA}copy garee linkiga hoose kadibna udir targeetka"
  echo -e "${BLUE} http://127.0.0.1:8080${NC}"
  echo -e "${MAGENTA}----------------------------------"
     python mod.py
elif [ "$doorro" = "2" ]; then
  echo -e " ${YELLOW}waad ku mahadsantahay isticmaalka programkan waxaad igala soo xidhiidhi kartaa${NC}"
  echo -e "WHATSAPP: ${WHITE} +251992925681${NC}"
  echo -e "GMAIL:  ${WHITE}   baalkool12345@gmail.com${NC} "
fi

exit

else
  echo -e "${RED}Invalid input. Please select a valid option.${NC}"

fi

exit
