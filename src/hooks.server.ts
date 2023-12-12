/** @type {import('@sveltejs/kit').Handle} */
import { redirect } from '@sveltejs/kit';


export async function handle({ event, resolve }) {

    if (event.url.pathname.startsWith('/admin')) {
        const access_token = event.cookies.get('access_token');

        if (!access_token) {
            throw redirect(303, "/login");
        }
    }

    const response = await resolve(event);
    return response;
}