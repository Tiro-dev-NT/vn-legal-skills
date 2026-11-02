import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:flutter_contacts/flutter_contacts.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  MobileAds.instance.initialize();
  runApp(const UngDungMau());
}

class UngDungMau extends StatelessWidget {
  const UngDungMau({super.key});

  Future<void> taiDuLieu() async {
    final viTri = await Geolocator.getCurrentPosition();
    final danhBa = await FlutterContacts.getContacts(withProperties: true);
    debugPrint('${viTri.latitude} ${danhBa.length}');
  }

  @override
  Widget build(BuildContext context) {
    final quangCao = BannerAd(
      adUnitId: 'ca-app-pub-0000000000000000/0000000000',
      size: AdSize.banner,
      request: const AdRequest(),
      listener: const BannerAdListener(),
    )..load();
    return MaterialApp(home: Scaffold(body: AdWidget(ad: quangCao)));
  }
}
