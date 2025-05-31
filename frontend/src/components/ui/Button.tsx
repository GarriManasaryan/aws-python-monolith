'use client';

import React from 'react';

interface ButtonProps {
    children: React.ReactNode;
    className?: string;
}

export const Button: React.FC<ButtonProps> = ({ children, className }) => (
    <button className={`px-4 py-2 bg-blue-600 text-white rounded ${className}`}>
        {children}
    </button>
);
