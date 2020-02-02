function showExample(){
    $("#input_gene").val("EGFR");
    $("#input_fusion").val("EGFR--VSTM2A");
    $("#input_tumortype").val("LGG");
    $("#input_run").val("SRR934846");
    $("#input_chr").val("chr7");
    $("#input_pos").val("55200413");
    $("#input_range").val("1000")
}

function clearAll(){
    $("#input_gene").val("");
    $("#input_fusion").val("");
    $("#input_tumortype").val("");
    $("#input_run").val("");
    $("#input_chr").val("");
    $("#input_pos").val("");
    $("#input_range").val("")
}

function query() {

  $("#search_result").empty();
  $("#search_button").attr('disabled', true);

  var access = new Array();
  $.each($("input[name='access']:checked"),function(){
        access.push($(this).val())
  });

  $.ajax({
    url: "/sample",
    type: 'POST',
    dataType: 'json',
    data: {
      geneSymbol: $("#input_gene").val(),
      fusionName: $("#input_fusion").val(),
      tumorType: $("#input_tumortype").val(),
      runId: $("#input_run").val(),
      chr: $("#input_chr").val(),
      pos: $("#input_pos").val(),
      range: $("#input_range").val(),
      accessContent: access
    },
    success: function (res) {
      var data = res.data;
      var basic_keys = [
        "FusionName",
        "dataset",
        "Run",
        "Phenotype",
        "SpliceType",
        "known_fusion_disease",
        "JunctionReads",
        "JunctionReadCount",
        "SpanningFrags",
        "SpanningFragCount"
      ];
      var gene_keys = [
        "LeftGene",
        "left_gene",
        "leftgene_symbol",
        "LeftBreakpoint",
        "RightGene",
        "right_gene",
        "rightgene_symbol",
        "RightBreakpoint"
      ];

      var advance_keys = [
        "chromtype",
        "fusion_type"
      ];

      var leave_keys = [
        "LeftBreakpointChr",
        "LeftBreakpointPos",
        "LeftBreakpointSymbol",
        "RightBreakpointChr",
        "RightBreakpointPos",
        "RightBreakpointSymbol"
      ];

      formatThead(basic_keys, "#search_result");

      if (data != null){
        formatTbody(data, basic_keys, gene_keys, advance_keys, leave_keys, "#search_result")
      }

      $("#search_result").show();
      $("#search_button").attr('disabled', false);

    },
    error: function (err) {
      console.warn(JSON.stringify(err));
    }
  });
}

function formatThead(keys, appendnode) {
  // 添加表头
  var $trHead = $("<tr></tr>");

  for (i = 0; i < keys.length; i++) {
    $trHead.append("<th>" + keys[i] + "</th>");
  }

  $trHead.appendTo(appendnode);

}

function formatTbody(data, headkeys, genekeys, advancekeys, leftkeys, appendnode) {

  // 添加内容，一条数据是一行
  for (var i = 0; i < data.length; i++) {

    var data_i = data[i];

    // 添加主要显示内容
    var $trMain = $("<tr class='main'></tr>");

    for (j = 0; j < headkeys.length; j++) {

      var head_j = headkeys[j];

      if (j == 0) {
        $trMain.append("<td onclick='showDetail(this)'>" + "<a>" + data_i[head_j] + "</a>" + "</td>");
      }
      else if (j == 1) {
        $trMain.append("<td>" + "<a href='https://www.ncbi.nlm.nih.gov/sra/" + data_i[head_j] + "' target='_blank'>" + data_i[head_j] + "</a>" + "</td>");
      }
      else if (j == 2) {
        $trMain.append("<td>" + "<a href='https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=" + data_i[head_j] + "' target='_blank'>" + data_i[head_j] + "</a>" + "</td>");
      }
      else {
        $trMain.append("<td>" + data_i[head_j] + "</td>");
      }
      ;
    }

    $trMain.appendTo(appendnode);

    // 添加详细信息
    var $trDetail = $("<tr class='detail' style='display:none'></tr>");
    var $tdDetail = $("<td colspan=13></td>")

    // 详细信息的表格
    var $detail_table = $("<table class='table table-bordered table-hover text-nowrap'></table>");
    var $gene_tr = $("<tr></tr>") //基因信息
    var $advance_tr = $("<tr></tr>") //高级信息
    var $other_tr = $("<tr></tr>") //其他信息
    var $structure_tr = $("<tr></tr>") //结构信息
    var gene_detail = ""
    var advance_detail = ""
    var other_detail = ""

    for (x in data_i) {

      var label_val = data_i[x];

      if (genekeys.indexOf(x) != -1) {

        if (x == "leftgene_symbol" || x == "rightgene_symbol")
        {   
            label_val = "<a href='https://www.genecards.org/cgi-bin/carddisp.pl?gene=" + label_val + "' target='_blank'>" + label_val + "</a>";
        }

        gene_detail += "<label>" + x + "</label>" + " : " + label_val + "<br>";
      }
      else if (advancekeys.indexOf(x) != -1) {
        advance_detail += "<label>" + x + "</label>" + " : " + label_val + "<br>";
      }
      else if (headkeys.indexOf(x) == -1 && x != "id" && x != "sampleId" && leftkeys.indexOf(x) == -1) {
        other_detail += "<label>" + x + "</label>" + " : " + label_val + "<br>";

      }
    }

    $detail_table.append("<tr><th>基因信息:</th></tr>")
    $gene_tr.append("<td colspan='13'>" + gene_detail + "</td>")
    $gene_tr.appendTo($detail_table);

    $detail_table.append("<tr><th>高级信息:</th></tr>")
    $advance_tr.append("<td colspan='13'>" + advance_detail + "</td>")
    $advance_tr.appendTo($detail_table);
    $detail_table.append("<tr><td>基因：标记出kinase, TF, oncogene, Tumor suppressor基因,相关的药物</td><tr>")
    $detail_table.append("<tr><td>     融合基因的IGV断点read展示</td><tr>")
    $detail_table.append("<tr><td>注释：如果是注释的融合，给出注释的文献信息/数据库信息；如果不是已知的注释，对于参与融合的基因进行注释；新颖的融合基因</td><tr>")

    $detail_table.append("<tr><th>结构/功能预测:</th></tr>")
    $detail_table.append("<tr><td>信息待补充</td></tr>")

    $detail_table.append("<tr><th>其他信息:</th></tr>")
    $other_tr.append("<td colspan='13'>" + other_detail + "</td>")
    $other_tr.appendTo($detail_table);

    $detail_table.appendTo($tdDetail);
    $tdDetail.appendTo($trDetail);
    $trDetail.appendTo(appendnode);
  }
  ;
}

function showDetail(tr) {
  $(tr).parent().next().toggle();
}

function selectRun(td) {
  $("#select_type").val('run');
  $("#input").val($(td).text());
  console.log($("#select_type").val())
  console.log($("#input").val())
  query();
}
