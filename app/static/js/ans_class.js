function GetAnswer(){
    this.AnsJson = {};

}

GetAnswer.prototype.pushAns = function(q_type, index, value){
    this.AnsJson[index] = {value:value, type:q_type};
}

GetAnswer.prototype.getUrlVars = function(index){
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf(index) + 1).split('/');
    for(var i = 0; i < hashes.length; i++){
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

GetAnswer.prototype.Exam_start_end = function(time_flag, t_type){
    this.AnsJson["student_id"]=11;
    this.AnsJson[t_type]=time_flag;
    //~ alert(JSON.stringify(this.AnsJson))
}


