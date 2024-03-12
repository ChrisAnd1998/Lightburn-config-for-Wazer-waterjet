<?php

// Read the JSON file
$jsonData = file_get_contents('materialdata.json');

// Decode the JSON data
$data = json_decode($jsonData, true);

// Check if decoding was successful
if ($data === null) {
    echo "Error decoding JSON data\n";
    exit(1);
}

$xmlString = '<?xml version="1.0" encoding="UTF-8"?>';
$xmlString .= '<LightBurnLibrary>';

echo htmlspecialchars($xmlString);

// Iterate over each entry and echo the "_id" value
foreach ($data as $entry) {

    //if (str_contains($entry['thickness'], 'mm')) {
        $xmlString = '<Material name="'.$entry['name'].'">';
        $xmlString .= '<Entry Thickness="-1.0000" Desc="Speed: '.$entry['speedFineRate'].' Pierce: '.$entry['pierceTime'].'" NoThickTitle="'.$entry['thickness'].'">';
        $xmlString .= '<CutSetting type="Cut">';
        $xmlString .= '<index Value="0"/>';
        $xmlString .= '<name Value=""/>';
        $xmlString .= '<LinkPath Value="'.$entry['name'].'/'.$entry['thickness'].'/'.str_replace('&','and',$entry['category']).'"/>';
        $xmlString .= '<minPower Value="4"/>';
        $xmlString .= '<maxPower Value="100"/>';
        $xmlString .= '<maxPower2 Value="20"/>';
        $xmlString .= '<speed Value="' . ((str_replace('in/min','',(str_replace('mm/min','',$entry['speedFineRate']))))) / 60 . '"/>';
        $xmlString .= '<startDelay Value="' . str_replace('s','',$entry['pierceTime']) . '"/>';
        $xmlString .= '<leadIn Value="1"/>';
        $xmlString .= '<leadLength Value="5"/>';
        $xmlString .= '<leadAngle Value="90"/>';
        $xmlString .= '<leadStyle Value="arc"/>';
        $xmlString .= '<priority Value="0"/>';
        $xmlString .= '<tabCount Value="1"/>';
        $xmlString .= '<tabCountMax Value="1"/>';
        $xmlString .= '</CutSetting>';
        $xmlString .= '</Entry>';
        $xmlString .= '</Material>';

        echo htmlspecialchars($xmlString);
    //}
    
}

// End the XML string
$xmlString = '</Material>';
$xmlString .= '</LightBurnLibrary>';

// Output the XML string
echo htmlspecialchars($xmlString);

?>
