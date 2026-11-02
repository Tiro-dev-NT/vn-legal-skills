import { createClient } from '@supabase/supabase-js';
import ManDangNhap from './screens/ManDangNhap';
import ManHoSo from './screens/ManHoSo';

export const supabase = createClient('https://mau-gia-lap.supabase.co', process.env.EXPO_PUBLIC_SUPABASE_ANON);

export default function App() {
  return <ManDangNhap />;
}
