function selectChange(){
    if ($("#select_type").val()=="gene")
    {   
       $("#chr").hide()
       $("#pos").hide()
       $("#range").hide()
       $("#normal").show()
       $("#input").val("EGFR");
    }
    else if ($("#select_type").val()=="fusion")
    {
       $("#chr").hide()
       $("#pos").hide()
       $("#range").hide()
       $("#normal").show()
       $("#input").val("EGFR--VSTM2A");
    }
    else if ($("#select_type").val()=="tumor")
    {
      $("#chr").hide()
      $("#pos").hide()
      $("#range").hide()
      $("#normal").show()
      $("#input").val("AML");
    }
    else if ($("#select_type").val()=="run")
    {
      $("#chr").hide()
      $("#pos").hide()
      $("#range").hide()
      $("#normal").show()
      $("#input").val("SRR934846");
    }
    else if ($("#select_type").val()=="breakpoint")
    {
      $("#normal").hide()
      $("#chr").show();
      $("#pos").show();
      $("#range").show();
    }

}

function query(){

    $("#search_result").empty();
    $("#search_button").attr('disabled',true);

    var select_type = $("#select_type");
    

    if (select_type.val()=="breakpoint"){
        var chr = $("#input_chr")
        var pos = $("#input_pos")
        var range = $("#input_range")
        var query_url = "http://127.0.0.1/chr/" + chr.val() + "/pos/" + pos.val() +"/range/" + range.val()
    }
    else{
        var input = $("#input");
        var query_url = "http://127.0.0.1/" + select_type.val() + "/" + input.val()
    };

    $.get(query_url,function(res){
        if (res.status == 200){
            var data = res.data;
            var table = $("#search_result");
            var main_keys = [
                "FusionName",
                "fusion_type",
                "chromtype",
                "Phenotype",
                "Run",
                "SpliceType",
                "dataset",
                "JunctionReadCount",
                "SpanningFragCount",
                "RightBreakpoint",
                "LargeAnchorSupport",
                "annots",
                "known_fusion"
            ];
            var leave_keys = [
                "LeftBreakpointChr",
                "LeftBreakpointPos",
                "LeftBreakpointSymbol",
                "RightBreakpointChr",
                "RightBreakpointPos",
                "RightBreakpointSymbol"
            ];
            // 添加表头
            var $trHead = $("<tr></tr>");

            for (i=0;i<main_keys.length;i++){
                $trHead.append("<th>"+ main_keys[i] +"</th>");
            }
            
            $trHead.appendTo("#search_result");

            // 添加内容，一条数据是一行
            for( var i = 0;i< data.length; i++) {

                var data_i = data[i];

                // 添加主要显示内容
                var $trMain = $("<tr class='main'></tr>");

                for (j=0;j<main_keys.length;j++){

                    var head_j = main_keys[j];

                    if (j==0){
                        $trMain.append("<td onclick='showDetail(this)'>" + "<a>" +data_i[head_j] + "</a>" + "</td>");
                    }
                    else if (j==4){
                        $trMain.append("<td onclick='selectRun(this)'>"+ "<a>"+ data_i[head_j] + "</a>"+"</td>");
                    }
                    else if (j==6){
                        $trMain.append("<td>"+ "<a href='https://www.ncbi.nlm.nih.gov/sra/" + data_i[head_j] + "' target='_blank'>"+ data_i[head_j] + "</a>"+"</td>");
                    }
                    else {
                        $trMain.append("<td>"+ data_i[head_j] +"</td>");
                    };
                };

                $trMain.appendTo("#search_result");

                // 添加详细信息
                var $trDetail = $("<tr class='detail' style='display:none'></tr>");

                var detail_info = "";

                for (x in data_i){
                    if (main_keys.indexOf(x) == -1 && x!="id" && leave_keys.indexOf(x) == -1){

                        var label_val = data_i[x];

                        if (x == "leftgene_symbol" || x == "rightgene_symbol")
                        {   
                            label_val = "<a href='https://www.genecards.org/cgi-bin/carddisp.pl?gene=" + label_val + "' target='_blank'>" + label_val + "</a>";
                        }
                        
                        var row_info = "<label>" + x + "</label>" + " : " + label_val + "<br>";
                        detail_info += row_info;
                    }
                }

                $trDetail.append("<td colspan='13'>" + detail_info + "</td>")
                $trDetail.appendTo("#search_result");
            };
        };
        $("#search_result").show()
        $("#search_button").attr('disabled',false)
    });
}

function showDetail(tr){
    $(tr).parent().next().toggle();
}

function selectRun(td){
    $("#select_type").val('run');
    $("#input").val($(td).text());
    console.log($("#select_type").val())
    console.log($("#input").val())
    query();
}