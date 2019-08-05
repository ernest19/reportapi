// var mymap = L.map('mapid', {
//     maxBounds: L.latLngBounds([3.7388, -4.262], [12.1748, 2.200]),
//     measureControl: false,
//     minZoom: 1,
//     maxZoom: 19,
// }).setView([7.099, -1.000], 8);


// L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}', {
//     subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
// }).addTo(mymap);


   var mymap = L.map('mapid',{ maxBounds:L.latLngBounds([3.7388,-4.262],[12.1748,2.200]),}).setView([9.099, -1.000], 7);

   googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(mymap);





regionmap('/galamsey/regionboundary/NONE/', newregion, onEachFeaturereg)

function regionmap(url, mnh, oneach) {
    // removela(map, regmap)
    loaderbar('#oveli',true)
    $.get(url, function(data) {
        regmap = new L.GeoJSON(data, { style: mnh, onEachFeature: oneach }).addTo(mymap).bringToBack();
        // removelaturn(regmap, true)
    }).done(function() {
        $('#regcheck').prop('disabled', false)
        loaderbar('#oveli',false)
        // districtmapdrawn('/mapApp/districtboundary/NONE/',newdistrict,onEachFeaturedis)

    }).fail(function() {
        // loaderbar('.regc.circlemainsmall',false)
    });
}

function onEachFeaturereg(feature, layer) {
    // maplabel(layer, feature.properties['region_name'] + ' REGION');
    layer.on({
        click: zoomToFeaturer
    });
}




$('#regcheck').on('change',function(){
  var man = $('#regcheck').is(':checked');
  if (man == true){
    if (regmap) {
       mymap.addLayer(regmap);
        // map.addLayer(regioncapital);
      removelaturn(regmap, true)
    }
  }
  else
  {
    mymap.removeLayer(regmap);
    // map.removeLayer(regioncapital);
  }
})



$('#districtcheck').on('change',function(){
  var man = $('#districtcheck').is(':checked');
  // if (dismap == undefined){
  //   districtmapdrawn('/mapApp/districtboundary/NONE/',newdistrict,onEachFeaturedis)
  // }
  if (man == true){ 
    if (dismap) {
      mymap.addLayer(dismap);
      // map.addLayer(districtcapital);
      removelaturn(dismap,true)
      removelaturn(regmap,true)
    
    }
    
  }
  else
  {
    mymap.removeLayer(dismap);
   // map.removeLayer(districtcapital);
  }
})



function removelaturn(dat,tru){
  if (dat != undefined){
        if (tru == true){
          dat.bringToBack()
        }else{
          dat.bringToFront()
        }
    }
}





function newregion() {
    return {
        fillColor: 'transparent',
        color: 'red',
        weight: '3',
        dashArray: '',
        opacity: '1',
        fillOpacity: '0',
    };
}


function zoomToFeaturer(e) {
    map.fitBounds(e.target.getBounds());
    // selectpolygon(e.target.feature.id);
    // stateofhousehold = true;
    // stateofcom = false;
    // $('#inputcodecode').val(e.target.feature.id)
    // $('.overallhh').addClass('hidden');
    // $('.overallcom').removeClass('hidden');
}

function newdistrict() {
    return {
      fillColor: 'transparent',
      color: '#499',
      weight: '1.5',
      dashArray: '',
      opacity: '0.7',
      fillopacity: '0',
    };
      
}


function loaderbar(loadbar,valeu){
  if (valeu == true){
    $(loadbar).removeClass('hidden')
  }else if (valeu == false){
    $(loadbar).addClass('hidden')
  }
}




districtnmap('/galamsey/district/', newdistrict, district_onEachFeature)
function districtnmap(url, mnh, oneach) {
    // removela(map, regmap)
    loaderbar('#oveli',true)
    $.get(url, function(data) {
        dismap = new L.GeoJSON(data, { style: mnh, onEachFeature: oneach }).addTo(mymap);
        // removelaturn(regmap, true)
    }).done(function() {
        $('#districtcheck').prop('disabled', false)
        loaderbar('#oveli',false)
        // districtmapdrawn('/mapApp/districtboundary/NONE/',newdistrict,onEachFeaturedis)

    }).fail(function() {
        // loaderbar('.regc.circlemainsmall',false)
    });
}

function onEachFeaturereg(feature, layer) {
    // maplabel(layer, feature.properties['region_name'] + ' REGION');
    layer.on({
        click: zoomToFeaturer
    });
}





function district_onEachFeature(feature, layer) {
    layer.bindTooltip('</b>District Name:<b>' + totitlefunction(feature.properties.district_name), {direction: 'auto' })
    layer.on({
        mouseover: highlightFeature,
        mouseout: district_resetHighlight,
        click: zoomToFeature
    });
}




function highlightFeature(e) {
    var layer = e.target;
    layer.setStyle({
        weight: 5,
        color: '#203F73',
        dashArray: '',
        fillOpacity: 0,
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}



function district_resetHighlight(e) {
    dismap.resetStyle(e.target);
}



function zoomToFeature(e) {
    mymap.fitBounds(e.target.getBounds());
}


function totitlefunction(txt){
          var currVal = txt;
          currVal = currVal.toLowerCase().replace(/\b[a-z]/g, function(txtVal) {
            return txtVal.toUpperCase();
          });
          return currVal;
}






















signage('/charcoal/charcoalreportspoint/');


var ir;
function signage(url){
 if (ir != undefined){
      mymap.removeLayer(ir);
   }
    $("#oveli").removeClass("hidden")
    // map.spin(true);
   $.get(url, function(data){
    ir = new L.GeoJSON(data,{pointToLayer: function (feature, latlng){
      var check_status= feature.properties['status']
  
      if (check_status=='owes'){

        var baseballIcon = L.icon({iconUrl: '/static/Map/map/img/poor.png',iconSize: [30, 30]});
      }
      else{

        var baseballIcon = L.icon({iconUrl: '/static/img/point.gif',iconSize: [30, 30]});
      }
      
        
      //var icon2 = new L.divIcon({icon: 'mydivicon2', html:  ,iconSize:[20,20]});
    return L.marker(latlng, {icon: baseballIcon});
},
onEachFeature: function(feature, layer) {
      html = ('<div class="row" style="margin-left:2%"> ')
       html += ('<table class="table-bordered"> ')
       html += ('<tr class="table-row"><td> <b> Description </b></td><td>' + feature.properties['description'] + '</td><td rowspan="6"> <a class="fancybox" rel="ligthbox" href="/media/'+feature.properties['image']+'" title="' + feature.properties['project_community'] + '"><img src="/media/'+feature.properties['image']+'" alt="" style="width:100px; height:100px;" /></a></p> </td></tr>')
        html += ('<tr><td><b>Status</b><td>'+feature.properties['status']+'')

       html += ('</table>')
       html += ('</div >')

       layer.bindPopup(html, { maxWidth: "auto" });
       layer.on({ click: zoomToFeaturerproject });

      }}).addTo(mymap);
  }).done(function() {
      // map.spin(false);
      $("#overlayZZ").addClass("hidden")
        })
}




$('#pointcheck').on('change',function(){
  var man = $('#pointcheck').is(':checked');
  if (man == true){
    if (ir) {
       mymap.addLayer(ir);
        // map.addLayer(regioncapital);
      removelaturn(ir, true)
    }
  }
  else
  {
    mymap.removeLayer(ir);
    // map.removeLayer(regioncapital);
  }
})












   // function zoomToFeaturerproject(e) {
   //     mymap.fitBounds(e.target.getBounds());
   // }

function zoomToFeaturerproject(e)
{
  var latLngs = [e.target.getLatLng()];
  var markerBounds = L.latLngBounds(latLngs);
  mymap.fitBounds(markerBounds);
}





function getextent(projectvalue){
    $.get('/charcoal/extenta/?valuecode=' + projectvalue ,function(data){
            mymap.fitBounds([[data[1] ,data[0]],[data[3], data[2]]])
    })
}



