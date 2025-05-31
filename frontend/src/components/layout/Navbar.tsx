'use client';

import Link from 'next/link';

export const Navbar = () => (
    <nav className="flex justify-between items-center p-4 bg-gray-100">
        <Link href="/">Home</Link>
        <Link href="/about">About</Link>
    </nav>
);
