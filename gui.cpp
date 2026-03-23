#include <iostream>
#include <fstream>


class BotController {
private:
std::string command;
std::string status;

public:
BotController(std::string c,std::string s){
    command = c;
    status = s;

}

std::string getcommand(){
    return command;
}

std::string getstatus(){
    return status;
}
// this is getter

void write(std::string w){

    std::ofstream file("H:\\code\\c+++\\c+\\.vscode\\repo\\discordbot\\command.txt");
    file << w;
    file.close();


}

void read(){
    std::string a;
    std::ifstream read("H:\\code\\c+++\\c+\\.vscode\\repo\\discordbot\\status.txt");
    std::getline(read,a);
    std::cout << a << '\n';
}

~BotController(){
    std::cout << "destroyed" << '\n';
}

};

int main(){

BotController bot("command.txt","status.txt");
int choice;

do {
    std::cout << "1- JOIN_VC" << '\n';
    std::cout << "2- SEND" << '\n';
    std::cout << "3- BAN" << '\n';
    std::cout << "4- DM" << '\n';
    std::cout << "5- STATUS" << '\n';
    std::cout << "6- EXIT" << '\n';

    std::cout << "Enter your choice: " ;
    std::cin >> choice ;
    std::cout << '\n';
    if (choice == 1) {
        bot.write("JOIN_VC");
    }else if (choice == 2){
        std::string message;
        std::cout << "Enter message: ";
        std::cin >> message;
        std::cout << '\n';
        bot.write("SEND:" + message);
    }else if (choice==3){
        std::string username;
        std::cout << "Enter username: " ;
        std::cin >> username;
        std::cout << '\n';
        bot.write("BAN:" + username);
    }else if(choice==4){
        
        std::string user;
        std::string mess;
        std::cout << "Enter username: " ;
        std::cin >> user;
        std::cout << '\n';
        std::cout << "Enter message: " ;
        std::cin >> mess;
        std::cout << '\n';
        bot.write("DM:" + user + ":" + mess);
    }else if(choice==5){
        bot.read();
    }


}while(choice != 6);
 std::cout << "you are exited" << '\n';



}