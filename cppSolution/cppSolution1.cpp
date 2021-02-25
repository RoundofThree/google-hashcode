#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <utility>
using namespace std;

//read file to lines and store in a vector
vector<string> parseFile(string name){
    std::ifstream input_file;
    input_file.open(name);
    std::string line;
    std::vector<std::string> output_vector;
    while (getline(input_file, line))
    {
        std::istringstream ss_line(line);
        while(ss_line){
            std::string element;
            ss_line >> element;
            output_vector.push_back(element);
        }
    }
    return output_vector;
}

//read first line to vector of int
vector<int> getDetails(string str){
    vector<int> nums;
    stringstream ss;
    ss << str;

    string temp;
    int found;

    while (!ss.eof()) {
        ss >> temp;

        if (stringstream(temp) >> found)
           nums.push_back(found);
    }
    return nums;
}

//return all streets and its associated intersection
map<string, vector<int>> getStreetIntersection(int numStr, vector<string> const &v){
    map<string, vector<int>> streetDetail;
    for(int i = 1; i < numStr +1; ++i){
        int inInt = 0;
        int outInt = 0;
        int duration;
        string streetName ="";
        stringstream ss(v[i]);
        ss >> inInt >> outInt >> streetName >> duration;
        vector<int> values;
        values.push_back(inInt);
        values.push_back(outInt);
        values.push_back(duration);
        streetDetail.insert({streetName, values});
    }
    return streetDetail;
}

//add all path to vector, each vector represent a car path
vector<vector<string>> getPaths(int start, vector<string> const &v){
    vector<vector<string>> paths;
    for(int i = start +1; i < v.size(); ++i){
        stringstream ss;
        string str = v[i];
        ss << str;

        string temp;
        int found;
        vector<string> path;
        while(!ss.eof()){
            ss >> temp;
            if(!(stringstream(temp) >> found)){
               path.push_back(temp);
            }
        }
        paths.push_back(path);
    }

    return  paths;
}

//remove all unreachable destination within given time frame
vector<vector<string>> possiblePaths(int duration, vector<vector<string>> &paths, map<string, vector<int>> streetDetail){
    vector<vector<string>> possible;
    map<int, vector<string>> maPpossible;

    for(int i = 0; i < paths.size(); ++i){
        int total = 0;
        for(int x = 0; x < paths[i].size(); ++x){
            string name = paths[i][x];
            total += streetDetail.at(name).back();
        }

        if(total <= duration){
            maPpossible.insert({total, paths[i]});
        }

    }

    for(map<int, vector<string>>::iterator it = maPpossible.begin(); it  != maPpossible.end() ; ++it){
        possible.push_back(it ->second);
    }

    return possible;
}

// greedy Appracoach
void solveShoertestTimevector(vector<vector<string>> paths){
    
}
int main() {
    string file;
    cin >> file;
    vector<string> v = parseFile(file);
    vector<int> nums = getDetails(v[0]);
    int duration = nums[0];
    int numInters = nums[1];
    int numStr = nums[2];
    int numCars = nums[3];
    int reward = nums[4];
    map<string, vector<int>> streetDetail = getStreetIntersection(numStr, v);
    vector<vector<string>> paths = getPaths(numStr, v);
    //remove all unpossible
    paths = possiblePaths(duration, paths, streetDetail);



    return 0;
}